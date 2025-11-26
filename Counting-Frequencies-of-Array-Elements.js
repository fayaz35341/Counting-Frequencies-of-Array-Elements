class Solution {
    countFrequencies(nums) {
        const visited = new Set();
        const result = [];

        for (let i = 0; i < nums.length; i++) {
            if (visited.has(nums[i])) continue;

            let count = 0;
            for (let j = 0; j < nums.length; j++) {
                if (nums[i] === nums[j]) {
                    count++;
                }
            }

            result.push([nums[i], count]);
            visited.add(nums[i]);
        }
        return result;
    }
}
const n = [1, 2, 2, 1, 3];
console.log(new Solution().countFrequencies(n));
