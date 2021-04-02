using System;

namespace ttemma.Helpers.Math
{
	// Token: 0x02000004 RID: 4
	public static class MathHelper
	{
		// Token: 0x06000042 RID: 66 RVA: 0x00003774 File Offset: 0x00001D74
		public static int CalculateBlocksLength(int blockLength, int dataLength)
		{
			int num = dataLength / blockLength;
			int num2 = dataLength % blockLength;
			int num3 = num;
			if (num2 > 0)
			{
				num3++;
			}
			return num3 * blockLength;
		}
	}
}
