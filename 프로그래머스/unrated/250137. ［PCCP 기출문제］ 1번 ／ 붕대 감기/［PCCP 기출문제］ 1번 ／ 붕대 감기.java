class Solution {
    // bandage 시전 시간, 초당 회복량, 추가 회복량
    // health 체력
    public int solution(int[] bandage, int health, int[][] attacks) {
        int continuous = 0, idx = 0;
        int h = health;
        int time = attacks[attacks.length-1][0];
        boolean isAttack = false;

        while (idx != time) {
            idx += 1;

            // 몬스터가 공격한다면 체력 감소
            for (int[] attack : attacks) {
                if (attack[0] == idx) {
                    h -= attack[1];
                    continuous = 0;
                    isAttack = true;
                }
            }

            // 체력이 0이하라면 종료
            if (h <= 0) {
                h = -1;
                break;
            }

            if (isAttack) {
                isAttack = false;
                continue;
            }

            h += bandage[1];
            continuous += 1;

            // 연속으로 회복을 시전할 수 있는 시간이 지났다면 추가 회복량을 더해준다
            if (continuous == bandage[0]) {
                h += bandage[2];
                continuous = 0;
            }

            // 체력이 최대 체력을 넘어가면 최대 체력으로 고정
            if (h > health) {
                h = health;
            }

        }
        return h;
    }
}