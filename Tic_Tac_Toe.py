import math # Used for infinity (math.inf) to represent "worst possible score"
import tkinter as tk # The standard Python GUI library
from tkinter import messagebox # For the "Game Over" popups

# ==========================================
# PART 1: THE BACKEND (LOGIC & ALGORITHM)
# ==========================================
class TicTacToeBackend:
    def __init__(self):
        # Create a list of 9 empty spaces representing the 3x3 grid.
        # indices: 0 1 2
        #          3 4 5
        #          6 7 8
        self.board = [' ' for _ in range(9)] 
        self.human = 'X' # Human plays X
        self.ai = 'O'    # AI plays O

    def is_winner(self, player):
        """Checks if the given player ('X' or 'O') has won."""
        # A list of all 8 ways to win (3 rows, 3 cols, 2 diagonals)
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        # Loop through every winning combination
        for a, b, c in win_conditions:
            # Check if board positions a, b, and c ALL match the player
            if self.board[a] == player and self.board[b] == player and self.board[c] == player:
                return True # We found a winner!
        return False # Checked all 8 ways, no winner found.

    def is_board_full(self):
        """Returns True if there are no empty spaces (' ') left."""
        return ' ' not in self.board

    def get_available_moves(self):
        """Returns a list of numbers (indices) where the board is empty."""
        return [i for i, x in enumerate(self.board) if x == ' ']

    # --- THE BRAIN: MINIMAX ALGORITHM ---
    def minimax(self, board, depth, is_maximizing):
        """
        Recursive function to calculate the score of the board.
        depth: How many moves deep we are in the simulation.
        is_maximizing: True if it's AI's turn, False if Human's turn.
        """
        
        # 1. BASE CASES (Stop recursion if game is over)
        if self.is_winner(self.ai):
            return 10 - depth # AI wins! Prefer winning SOONER (smaller depth)
        if self.is_winner(self.human):
            return -10 + depth # Human wins. Prefer losing LATER (larger depth)
        if self.is_board_full():
            return 0 # Draw

        # 2. RECURSIVE STEP
        if is_maximizing:
            # AI's Turn: Start with the worst possible score (-Infinity)
            best_score = -math.inf
            
            # Try every empty spot
            for move in self.get_available_moves():
                board[move] = self.ai          # SIMULATE move
                score = self.minimax(board, depth + 1, False) # RECURSE (Switch turns)
                board[move] = ' '              # UNDO move (Backtracking)
                
                # Keep the highest score found so far
                best_score = max(score, best_score)
            return best_score
            
        else:
            # Human's Turn: Start with the worst possible score for AI (+Infinity)
            best_score = math.inf
            
            # Try every empty spot
            for move in self.get_available_moves():
                board[move] = self.human       # SIMULATE move
                score = self.minimax(board, depth + 1, True) # RECURSE (Switch turns)
                board[move] = ' '              # UNDO move
                
                # Keep the lowest score (Assume human plays perfectly)
                best_score = min(score, best_score)
            return best_score

    def get_best_move(self):
        """Called by the GUI to get the AI's final decision."""
        best_score = -math.inf
        best_move = None
        
        # Loop through valid moves for the ACTUAL board
        for move in self.get_available_moves():
            self.board[move] = self.ai    # Make move
            score = self.minimax(self.board, 0, False) # Call the brain
            self.board[move] = ' '        # Undo move
            
            # If this move results in a better score than we've seen, remember it
            if score > best_score:
                best_score = score
                best_move = move
                
        return best_move # Return the index (0-8) where AI wants to play

    def make_move(self, index, player):
        """Updates the real board. Returns True if successful."""
        if self.board[index] == ' ':
            self.board[index] = player
            return True
        return False

# ==========================================
# PART 2: THE FRONTEND (GUI & STYLING)
# ==========================================
class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Minimax Tic-Tac-Toe")
        
        # --- STYLING 1: WINDOW SETUP ---
        # Set window size (Width x Height)
        self.root.geometry("400x520") 
        # Set background color (Hex Code: #2c3e50 is Dark Blue-Grey)
        self.root.configure(bg="#2c3e50") 
        
        # Initialize logic
        self.game = TicTacToeBackend()
        self.buttons = []
        self.game_over = False

        # --- STYLING 2: TITLE LABEL ---
        # A header text at the top of the window
        title_label = tk.Label(root, text="Beat the AI", 
                               font=('Helvetica', 18, 'bold'), 
                               bg="#2c3e50", fg="#ecf0f1") # White text on dark bg
        title_label.pack(pady=20) # Add padding (vertical space)

        # Create a Frame to hold the grid (keeps it centered)
        grid_frame = tk.Frame(root, bg="#2c3e50")
        grid_frame.pack()

        # Create 9 buttons in a loop
        for i in range(9):
            # --- STYLING 3: BUTTON DESIGN ---
            btn = tk.Button(grid_frame, 
                            text=" ", 
                            font=('Arial', 20, 'bold'), 
                            height=2, width=5,
                            bg="#ecf0f1",       # Light Grey Background (Normal)
                            fg="#2c3e50",       # Dark Text
                            activebackground="#bdc3c7", # Color when you hold click
                            # Connect the click event to our function
                            command=lambda index=i: self.on_button_click(index))
            
            # Grid placement with padding (padx/pady) to create gaps between buttons
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)

        # --- STYLING 4: RESTART BUTTON ---
        # A separate button at the bottom to reset the game
        reset_btn = tk.Button(root, text="Restart Game", command=self.reset_game,
                              bg="#e74c3c", # Red background
                              fg="white",   # White text
                              font=('Arial', 12, 'bold'),
                              relief="flat", padx=10, pady=5)
        reset_btn.pack(pady=20)

    def on_button_click(self, index):
        """Triggered when a user clicks a grid button."""
        if self.game_over: return

        # --- STEP 1: HUMAN MOVE ---
        if self.game.make_move(index, self.game.human):
            # Update UI: Disable button and turn text GREEN (#27ae60)
            self.buttons[index].config(text=self.game.human, state="disabled", disabledforeground="#27ae60")
            
            if self.check_status(self.game.human): return

            # --- STEP 2: AI MOVE ---
            # Change cursor to 'watch' (hourglass) to show AI is thinking
            self.root.config(cursor="watch")
            self.root.update() # Force screen refresh

            ai_move = self.game.get_best_move()
            
            if ai_move is not None:
                self.game.make_move(ai_move, self.game.ai)
                # Update UI: Disable button and turn text RED (#c0392b)
                self.buttons[ai_move].config(text=self.game.ai, state="disabled", disabledforeground="#c0392b")
                self.check_status(self.game.ai)
            
            self.root.config(cursor="") # Reset cursor

    def check_status(self, player):
        """Checks for Win or Draw and shows a popup."""
        if self.game.is_winner(player):
            winner_name = "AI" if player == self.game.ai else "You"
            messagebox.showinfo("Game Over", f"{winner_name} won!")
            self.game_over = True
            return True
        
        if self.game.is_board_full():
            messagebox.showinfo("Game Over", "It's a Draw!")
            self.game_over = True
            return True
        return False

    def reset_game(self):
        """Resets the Logic and the UI to start over."""
        self.game = TicTacToeBackend() # Create fresh logic instance
        self.game_over = False
        
        # Reset all buttons to initial state
        for btn in self.buttons:
            btn.config(text=" ", state="normal", bg="#ecf0f1")

# Standard Python entry point
if __name__ == "__main__":
    root = tk.Tk()           # Create the main window
    app = TicTacToeGUI(root) # Start our game app
    root.mainloop()          # Keep window open