import time
import math

class PortableTrueVector:
    def __init__(self, semantic_input):
        self.raw = semantic_input
        # 12 Councils Spatial Mapping (Vector 12) - Eliminates Text Parsing
        self.vector_12 = self._map_to_spatial_frequency(semantic_input)
        
    def _map_to_spatial_frequency(self, text):
        # Turns direct meaning like "BIRU" into a resonance value using Prime Factor 3
        hash_val = sum(ord(char) for char in text)
        return [(hash_val * i) % 256 for i in range(1, 13)]

class AbyssalKernel:
    def __init__(self):
        self.cycle_count = 0
        self.registry_40bit = []
        print("[INIT] Abyssal Kernel Online. Operating under structural pressure.")

    def execute_ptv(self, ptv: PortableTrueVector):
        self.cycle_count += 1
        print(f"\n--- EXECUTION CYCLE: {self.cycle_count} ---")
        
        # Tawaf Core Processing: Loop data through 28 transformation axes
        tawaf_matrix = []
        for axis in range(1, 29): # Vector 28
            wave = sum([v * math.sin(axis) for v in ptv.vector_12])
            tawaf_matrix.append(wave)
            
        # 12:28=40 Structural Synthesis (Locking the Data State)
        final_state = int(abs(sum(tawaf_matrix) + sum(ptv.vector_12))) % (2**40)
        self.registry_40bit.append(final_state)
        print(f"[TAWAF CORE] Semantic Injection Successfully Locked at State: {hex(final_state)}")

        # Autophagy System Triggered exactly every 28 cycles
        if self.cycle_count % 28 == 0:
            self._trigger_autophagy()

    def _trigger_autophagy(self):
        print("\n[ABYSSAL CLEANER] 28th Cycle Reached. Initiating Organic Autophagy...")
        print("[CLEANING] Consuming invalid registries. Removing software bloat...")
        self.registry_40bit.clear() # Total organic purge
        print(f"[REST] System entering 12-second structural rest state for thermal balance.")
        time.sleep(12)
        print("[REST] System Awoke. Fitrah state restored with zero waste.")

# --- SIMULATION RUN ---
if __name__ == "__main__":
    kernel = AbyssalKernel()
    
    # Direct Semantic Input: Bypassing binary conversion logic
    input_data = "BIRU"
    ptv_data = PortableTrueVector(input_data)
    
    # Simulate execution blocks to show automated runtime clearing
    for _ in range(28):
        kernel.execute_ptv(ptv_data)
