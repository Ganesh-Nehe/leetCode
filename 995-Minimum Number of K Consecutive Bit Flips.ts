function minKBitFlips(nums: number[], k: number): number {
    const n = nums.length;
    let flips = 0;
    let flipCount = 0;
    const flipMarkers = new Array(n).fill(0);
    
    for (let i = 0; i < n; i++) {
        if (i >= k) {
            flipCount ^= flipMarkers[i - k];
        }

        if (nums[i] == (flipCount % 2)) {
            if (i + k > n) {
                return -1;
            }

            flipCount ^= 1;
            flipMarkers[i] = 1;
            flips++;
        }
    }
    
    return flips;
}
