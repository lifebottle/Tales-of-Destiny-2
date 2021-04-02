using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;

namespace ttemma.Helpers
{
	// Token: 0x02000003 RID: 3
	public class StreamHelper : IDisposable
	{
		// Token: 0x17000001 RID: 1
		// (get) Token: 0x06000001 RID: 1 RVA: 0x00002AC4 File Offset: 0x000010C4
		// (set) Token: 0x06000002 RID: 2 RVA: 0x00002AD1 File Offset: 0x000010D1
		public long Position
		{
			get
			{
				return this._stream.Position;
			}
			set
			{
				this._stream.Position = value;
			}
		}

		// Token: 0x17000002 RID: 2
		// (get) Token: 0x06000003 RID: 3 RVA: 0x00002ADF File Offset: 0x000010DF
		// (set) Token: 0x06000004 RID: 4 RVA: 0x00002AEC File Offset: 0x000010EC
		public long Length
		{
			get
			{
				return this._stream.Length;
			}
			set
			{
				this._stream.SetLength(value);
			}
		}

		// Token: 0x17000003 RID: 3
		// (get) Token: 0x06000005 RID: 5 RVA: 0x00002AFA File Offset: 0x000010FA
		// (set) Token: 0x06000006 RID: 6 RVA: 0x00002B02 File Offset: 0x00001102
		public ByteEncoding SelectedByteEncoding
		{
			get
			{
				return this._byteEncoding;
			}
			set
			{
				this.SetByteEncoding(value);
			}
		}

		// Token: 0x17000004 RID: 4
		// (get) Token: 0x06000007 RID: 7 RVA: 0x00002B0B File Offset: 0x0000110B
		public Stream Stream
		{
			get
			{
				return this._stream;
			}
		}

		// Token: 0x17000005 RID: 5
		// (get) Token: 0x06000008 RID: 8 RVA: 0x00002B13 File Offset: 0x00001113
		public Type StreamType
		{
			get
			{
				return this._streamType;
			}
		}

		// Token: 0x06000009 RID: 9 RVA: 0x00002B1B File Offset: 0x0000111B
		public StreamHelper(ByteEncoding byteEncoding = ByteEncoding.Little)
		{
			this._stream = new MemoryStream();
			this._streamType = typeof(MemoryStream);
			this.SetByteEncoding(byteEncoding);
		}

		// Token: 0x0600000A RID: 10 RVA: 0x00002B45 File Offset: 0x00001145
		public StreamHelper(Stream stream, ByteEncoding byteEncoding = ByteEncoding.Little, Type streamType = null)
		{
			this._stream = stream;
			this._streamType = (streamType ?? typeof(Stream));
			this.SetByteEncoding(byteEncoding);
		}

		// Token: 0x0600000B RID: 11 RVA: 0x00002B70 File Offset: 0x00001170
		public StreamHelper(string fileName, ByteEncoding byteEncoding = ByteEncoding.Little, FileMode fileMode = FileMode.OpenOrCreate, FileAccess fileAccess = FileAccess.ReadWrite, FileShare fileShare = FileShare.Read)
		{
			this._stream = new FileStream(fileName, fileMode, fileAccess, fileShare);
			this._streamType = typeof(FileStream);
			this.SetByteEncoding(byteEncoding);
		}

		// Token: 0x0600000C RID: 12 RVA: 0x00002BA0 File Offset: 0x000011A0
		public StreamHelper(List<byte> bytes, ByteEncoding byteEncoding = ByteEncoding.Little)
		{
			this.SetByteEncoding(byteEncoding);
			this._stream = new MemoryStream();
			this._streamType = typeof(MemoryStream);
			this._stream.Write(bytes.ToArray(), 0, bytes.Count);
			this.Position = 0L;
		}

		// Token: 0x0600000D RID: 13 RVA: 0x00002BF8 File Offset: 0x000011F8
		public StreamHelper(byte[] bytes, ByteEncoding byteEncoding = ByteEncoding.Little)
		{
			this.SetByteEncoding(byteEncoding);
			this._stream = new MemoryStream();
			this._streamType = typeof(MemoryStream);
			this._stream.Write(bytes, 0, bytes.Length);
			this.Position = 0L;
		}

		// Token: 0x0600000E RID: 14 RVA: 0x00002C45 File Offset: 0x00001245
		public void Dispose()
		{
			Stream stream = this._stream;
			if (stream == null)
			{
				return;
			}
			stream.Dispose();
		}

		// Token: 0x0600000F RID: 15 RVA: 0x00002C57 File Offset: 0x00001257
		public void SetByteEncoding(ByteEncoding byteEncoding)
		{
			if (byteEncoding == ByteEncoding.None)
			{
				this._byteEncoding = ByteEncoding.Little;
				return;
			}
			this._byteEncoding = byteEncoding;
		}

		// Token: 0x06000010 RID: 16 RVA: 0x00002C6B File Offset: 0x0000126B
		private void ThrowStreamEndException()
		{
			throw new Exception("#Error 0 - Stream end.");
		}

		// Token: 0x06000011 RID: 17 RVA: 0x00002C78 File Offset: 0x00001278
		private void ExecuteMethod(string typeMethod, string nameMethod, object[] param)
		{
			MethodInfo method = typeof(StreamHelper).GetMethod(typeMethod + nameMethod);
			if (method == null)
			{
				return;
			}
			method.Invoke(this, param);
		}

		// Token: 0x06000012 RID: 18 RVA: 0x00002CAF File Offset: 0x000012AF
		public byte ReadByte()
		{
			int num = this._stream.ReadByte();
			if (num == -1)
			{
				this.ThrowStreamEndException();
			}
			return (byte)num;
		}

		// Token: 0x06000013 RID: 19 RVA: 0x00002CC8 File Offset: 0x000012C8
		public void Read<T>(out T value, ByteEncoding byteEncoding = ByteEncoding.None) where T : struct
		{
			ByteEncoding byteEncoding2 = (byteEncoding == ByteEncoding.None) ? this._byteEncoding : byteEncoding;
			string name = typeof(T).Name;
			object obj = new object();
			if (name == "Byte")
			{
				this.ExecuteMethod("Read", name, new object[]
				{
					obj
				});
			}
			else
			{
				this.ExecuteMethod("Read", name, new object[]
				{
					obj,
					byteEncoding2
				});
			}
			value = (T)((object)obj);
		}

		// Token: 0x06000014 RID: 20 RVA: 0x00002D48 File Offset: 0x00001348
		public short ReadInt16(ByteEncoding byteEncoding = ByteEncoding.None)
		{
			if (((byteEncoding == ByteEncoding.None) ? this._byteEncoding : byteEncoding) == ByteEncoding.Little)
			{
				return (short)((int)this.ReadByte() | (int)this.ReadByte() << 8);
			}
			return (short)((int)this.ReadByte() << 8 | (int)this.ReadByte());
		}

		// Token: 0x06000015 RID: 21 RVA: 0x00002D7C File Offset: 0x0000137C
		public int ReadInt32(ByteEncoding byteEncoding = ByteEncoding.None)
		{
			ByteEncoding byteEncoding2 = (byteEncoding == ByteEncoding.None) ? this._byteEncoding : byteEncoding;
			if (byteEncoding2 == ByteEncoding.Little)
			{
				return (int)this.ReadUInt16(byteEncoding2) | (int)this.ReadInt16(byteEncoding2) << 16;
			}
			return (int)this.ReadInt16(byteEncoding2) << 16 | (int)this.ReadUInt16(byteEncoding2);
		}

		// Token: 0x06000016 RID: 22 RVA: 0x00002DC0 File Offset: 0x000013C0
		public long ReadInt64(ByteEncoding byteEncoding = ByteEncoding.None)
		{
			ByteEncoding byteEncoding2 = (byteEncoding == ByteEncoding.None) ? this._byteEncoding : byteEncoding;
			if (byteEncoding2 == ByteEncoding.Little)
			{
				return (long)((ulong)this.ReadUInt32(byteEncoding2) | (ulong)((long)this.ReadInt32(byteEncoding2)));
			}
			return (long)this.ReadInt32(byteEncoding2) | (long)((ulong)this.ReadUInt32(byteEncoding2));
		}

		// Token: 0x06000017 RID: 23 RVA: 0x00002E01 File Offset: 0x00001401
		public ushort ReadUInt16(ByteEncoding byteEncoding = ByteEncoding.None)
		{
			if (((byteEncoding == ByteEncoding.None) ? this._byteEncoding : byteEncoding) == ByteEncoding.Little)
			{
				return (ushort)((int)this.ReadByte() | (int)this.ReadByte() << 8);
			}
			return (ushort)((int)this.ReadByte() << 8 | (int)this.ReadByte());
		}

		// Token: 0x06000018 RID: 24 RVA: 0x00002E34 File Offset: 0x00001434
		public uint ReadUInt32(ByteEncoding byteEncoding = ByteEncoding.None)
		{
			ByteEncoding byteEncoding2 = (byteEncoding == ByteEncoding.None) ? this._byteEncoding : byteEncoding;
			if (byteEncoding2 == ByteEncoding.Little)
			{
				return (uint)((int)this.ReadUInt16(byteEncoding2) | (int)this.ReadUInt16(byteEncoding2) << 16);
			}
			return (uint)((int)this.ReadUInt16(byteEncoding2) << 16 | (int)this.ReadUInt16(byteEncoding2));
		}

		// Token: 0x06000019 RID: 25 RVA: 0x00002E78 File Offset: 0x00001478
		public ulong ReadUInt64(ByteEncoding byteEncoding = ByteEncoding.None)
		{
			ByteEncoding byteEncoding2 = (byteEncoding == ByteEncoding.None) ? this._byteEncoding : byteEncoding;
			return (ulong)(this.ReadUInt32(byteEncoding2) | this.ReadUInt32(byteEncoding2));
		}

		// Token: 0x0600001A RID: 26 RVA: 0x00002EA6 File Offset: 0x000014A6
		public void WriteByte(byte value)
		{
			this._stream.WriteByte(value);
		}

		// Token: 0x0600001B RID: 27 RVA: 0x00002EB4 File Offset: 0x000014B4
		public void Write<T>(T value, ByteEncoding byteEncoding = ByteEncoding.None) where T : struct
		{
			ByteEncoding byteEncoding2 = (byteEncoding == ByteEncoding.None) ? this._byteEncoding : byteEncoding;
			string name = typeof(T).Name;
			if (name == "Byte")
			{
				this.ExecuteMethod("Write", name, new object[]
				{
					value
				});
				return;
			}
			this.ExecuteMethod("Write", name, new object[]
			{
				value,
				byteEncoding2
			});
		}

		// Token: 0x0600001C RID: 28 RVA: 0x00002F2C File Offset: 0x0000152C
		public void WriteInt16(short value, ByteEncoding byteEncoding = ByteEncoding.None)
		{
			if (((byteEncoding == ByteEncoding.None) ? this._byteEncoding : byteEncoding) == ByteEncoding.Little)
			{
				this.WriteByte((byte)(value & 255));
				this.WriteByte((byte)(value >> 8 & 255));
				return;
			}
			this.WriteByte((byte)(value >> 8 & 255));
			this.WriteByte((byte)(value & 255));
		}

		// Token: 0x0600001D RID: 29 RVA: 0x00002F88 File Offset: 0x00001588
		public void WriteInt32(int value, ByteEncoding byteEncoding = ByteEncoding.None)
		{
			ByteEncoding byteEncoding2 = (byteEncoding == ByteEncoding.None) ? this._byteEncoding : byteEncoding;
			if (byteEncoding2 == ByteEncoding.Little)
			{
				this.WriteInt16((short)(value & 65535), byteEncoding2);
				this.WriteInt16((short)(value >> 16 & 65535), byteEncoding2);
				return;
			}
			this.WriteInt16((short)(value >> 16 & 65535), byteEncoding2);
			this.WriteInt16((short)(value & 65535), byteEncoding2);
		}

		// Token: 0x0600001E RID: 30 RVA: 0x00002FEC File Offset: 0x000015EC
		public void WriteInt64(long value, ByteEncoding byteEncoding = ByteEncoding.None)
		{
			ByteEncoding byteEncoding2 = (byteEncoding == ByteEncoding.None) ? this._byteEncoding : byteEncoding;
			if (byteEncoding2 == ByteEncoding.Little)
			{
				this.WriteInt32((int)(value & (long)(/*(ulong)*/-1)), byteEncoding2);
				this.WriteInt32((int)(value >> 32 & (long)(/*(ulong)*/-1)), byteEncoding2);
				return;
			}
			this.WriteInt32((int)(value >> 32 & (long)(/*(ulong)*/-1)), byteEncoding2);
			this.WriteInt32((int)(value & (long)(/*(ulong)*/-1)), byteEncoding2);
		}

		// Token: 0x0600001F RID: 31 RVA: 0x00002F2C File Offset: 0x0000152C
		public void WriteUInt16(ushort value, ByteEncoding byteEncoding = ByteEncoding.None)
		{
			if (((byteEncoding == ByteEncoding.None) ? this._byteEncoding : byteEncoding) == ByteEncoding.Little)
			{
				this.WriteByte((byte)(value & 255));
				this.WriteByte((byte)(value >> 8 & 255));
				return;
			}
			this.WriteByte((byte)(value >> 8 & 255));
			this.WriteByte((byte)(value & 255));
		}

		// Token: 0x06000020 RID: 32 RVA: 0x00003044 File Offset: 0x00001644
		public void WriteUInt32(uint value, ByteEncoding byteEncoding = ByteEncoding.None)
		{
			ByteEncoding byteEncoding2 = (byteEncoding == ByteEncoding.None) ? this._byteEncoding : byteEncoding;
			if (byteEncoding2 == ByteEncoding.Little)
			{
				this.WriteUInt16((ushort)(value & 65535U), byteEncoding2);
				this.WriteUInt16((ushort)(value >> 16 & 65535U), byteEncoding2);
				return;
			}
			this.WriteUInt16((ushort)(value >> 16 & 65535U), byteEncoding2);
			this.WriteUInt16((ushort)(value & 65535U), byteEncoding2);
		}

		// Token: 0x06000021 RID: 33 RVA: 0x000030A8 File Offset: 0x000016A8
		public void WriteUInt64(ulong value, ByteEncoding byteEncoding = ByteEncoding.None)
		{
			ByteEncoding byteEncoding2 = (byteEncoding == ByteEncoding.None) ? this._byteEncoding : byteEncoding;
			if (byteEncoding2 == ByteEncoding.Little)
			{
				this.WriteUInt32((uint)((uint)value & /*(ulong)*/-1), byteEncoding2);
				this.WriteUInt32((uint)((uint)value >> 32 & /*(ulong)*/-1), byteEncoding2);
				return;
			}
			this.WriteUInt32((uint)((uint)value >> 32 & /*(ulong)*/-1), byteEncoding2);
			this.WriteUInt32((uint)((uint)value & /*(ulong)*/-1), byteEncoding2);
		}

		// Token: 0x06000022 RID: 34 RVA: 0x00003100 File Offset: 0x00001700
		public byte[] ReadByteArray(int count)
		{
			byte[] array = new byte[count];
			int count2 = this._stream.Read(array, 0, count);
			return array.Take(count2).ToArray<byte>();
		}

		// Token: 0x06000023 RID: 35 RVA: 0x0000312F File Offset: 0x0000172F
		public List<byte> ReadByteList(int count)
		{
			return this.ReadByteArray(count).ToList<byte>();
		}

		// Token: 0x06000024 RID: 36 RVA: 0x0000313D File Offset: 0x0000173D
		public void WriteByteArray(byte[] array)
		{
			this._stream.Write(array, 0, array.Length);
		}

		// Token: 0x06000025 RID: 37 RVA: 0x0000314F File Offset: 0x0000174F
		public void WriteByteArray(byte[] array, int size)
		{
			this._stream.Write(array, 0, size);
		}

		// Token: 0x06000026 RID: 38 RVA: 0x0000315F File Offset: 0x0000175F
		public void WriteByteArray(byte[] array, int idx, int size)
		{
			this._stream.Write(array, idx, size);
		}

		// Token: 0x06000027 RID: 39 RVA: 0x0000316F File Offset: 0x0000176F
		public void WriteByteList(List<byte> listBytes)
		{
			this.WriteByteArray(listBytes.ToArray());
		}

		// Token: 0x06000028 RID: 40 RVA: 0x00003180 File Offset: 0x00001780
		public void WriteRepeatByte(byte value, int count)
		{
			byte[] array = new byte[count];
			for (int i = 0; i < count; i++)
			{
				array[i] = value;
			}
			this.WriteByteArray(array);
		}

		// Token: 0x06000029 RID: 41 RVA: 0x000031AC File Offset: 0x000017AC
		public void CopyPartFromByteArray(byte[] source, int size, int bufferSize = 4096)
		{
			if (size <= 0)
			{
				throw new Exception("#Error 2 - Array specified size is zero.");
			}
			if (source.Length < size)
			{
				size = source.Length;
			}
			if (bufferSize > size)
			{
				bufferSize = size;
			}
			int i = 0;
			while (i < size)
			{
				this._stream.Write(source, i, bufferSize);
				i += bufferSize;
				if (size - i < bufferSize)
				{
					bufferSize = size - i;
				}
			}
		}

		// Token: 0x0600002A RID: 42 RVA: 0x00003200 File Offset: 0x00001800
		public void CopyPartFromStream(Stream source, int size, int bufferSize = 4096)
		{
			if (size <= 0)
			{
				throw new Exception("#Error 2 - Stream specified size is zero.");
			}
			if (source.Length < (long)size)
			{
				size = (int)source.Length;
			}
			if (bufferSize > size)
			{
				bufferSize = size;
			}
			byte[] buffer = new byte[bufferSize];
			int count;
			while ((count = source.Read(buffer, 0, bufferSize)) != 0)
			{
				this._stream.Write(buffer, 0, count);
				size -= bufferSize;
				if (size < bufferSize)
				{
					bufferSize = size;
				}
			}
		}

		// Token: 0x0600002B RID: 43 RVA: 0x00003268 File Offset: 0x00001868
		public void CopyPartFromStream(Stream destination, int bufferSize = 4096)
		{
			this.CopyPartFromStream(destination, (int)destination.Length, bufferSize);
		}

		// Token: 0x0600002C RID: 44 RVA: 0x00003279 File Offset: 0x00001879
		public void CopyPartFromStreamHelper(StreamHelper source, int size, int bufferSize = 4096)
		{
			this.CopyPartFromStream(source._stream, size, bufferSize);
		}

		// Token: 0x0600002D RID: 45 RVA: 0x0000328C File Offset: 0x0000188C
		[Obsolete]
		public void CopyPartToByteArray(ref byte[] destination, int size, int bufferSize = 4096)
		{
			if (size <= 0)
			{
				throw new Exception("#Error 2 - Array specified size is zero.");
			}
			if (destination.Length < size)
			{
				size = destination.Length;
			}
			if ((long)size + this._stream.Position > this._stream.Length)
			{
				size = (int)(this._stream.Length - this._stream.Position);
			}
			if (bufferSize > size)
			{
				bufferSize = size;
			}
			byte[] array = new byte[bufferSize];
			int num = 0;
			int num2;
			while ((num2 = this._stream.Read(array, 0, bufferSize)) != 0)
			{
				Array.Copy(array, 0, destination, num, num2);
				num += num2;
				size -= num2;
				if (size == 0)
				{
					return;
				}
				if (size < bufferSize)
				{
					bufferSize = size;
				}
			}
		}

		// Token: 0x0600002E RID: 46 RVA: 0x00003330 File Offset: 0x00001930
		public byte[] CopyPartToByteArray(int size)
		{
			if (size <= 0)
			{
				throw new Exception("#Error 2 - Array specified size is zero.");
			}
			if ((long)size + this._stream.Position > this._stream.Length)
			{
				size = (int)(this._stream.Length - this._stream.Position);
			}
			return this.ReadByteArray(size);
		}

		// Token: 0x0600002F RID: 47 RVA: 0x00003388 File Offset: 0x00001988
		public void CopyPartToStream(Stream destination, int size, int bufferSize = 4096)
		{
			if (size <= 0)
			{
				throw new Exception("#Error 2 - Array specified size is zero.");
			}
			if (destination.Length < (long)size)
			{
				size = (int)destination.Length;
			}
			if ((long)size + this._stream.Position > this._stream.Length)
			{
				size = (int)(this._stream.Length - this._stream.Position);
			}
			if (bufferSize > size)
			{
				bufferSize = size;
			}
			byte[] buffer = new byte[bufferSize];
			int num;
			while ((num = this._stream.Read(buffer, 0, bufferSize)) != 0)
			{
				destination.Write(buffer, 0, num);
				size -= num;
				if (size < bufferSize)
				{
					bufferSize = size;
				}
			}
		}

		// Token: 0x06000030 RID: 48 RVA: 0x00003423 File Offset: 0x00001A23
		public void CopyPartToStreamHelper(StreamHelper destination, int size, int bufferSize = 4096)
		{
			this.CopyPartToStream(destination.Stream, size, bufferSize);
		}

		// Token: 0x06000031 RID: 49 RVA: 0x00003434 File Offset: 0x00001A34
		public string ReadAnsiString(int length, Encoding encoding)
		{
			byte[] array = new byte[length];
			this._stream.Read(array, 0, length);
			for (int i = 0; i < length; i++)
			{
				if (array[i] == 0)
				{
					length = i;
					break;
				}
			}
			return encoding.GetString(array, 0, length);
		}

		// Token: 0x06000032 RID: 50 RVA: 0x00003476 File Offset: 0x00001A76
		public string ReadAnsiString(int length, int codePage = 1252)
		{
			return this.ReadAnsiString(length, Encoding.GetEncoding(codePage));
		}

		// Token: 0x06000033 RID: 51 RVA: 0x00003488 File Offset: 0x00001A88
		public string ReadAnsiStringWithStopByte(Encoding encoding, byte stopByte = 0)
		{
			int num = 0;
			long position = this._stream.Position;
			while (this.ReadByte() != stopByte)
			{
				num++;
			}
			this.Position = position;
			string result = this.ReadAnsiString(num, encoding);
			long position2 = this.Position;
			this.Position = position2 + 1L;
			return result;
		}

		// Token: 0x06000034 RID: 52 RVA: 0x000034D2 File Offset: 0x00001AD2
		public string ReadAnsiStringWithStopByte(byte stopByte = 0, int codePage = 1252)
		{
			return this.ReadAnsiStringWithStopByte(Encoding.GetEncoding(codePage), stopByte);
		}

		// Token: 0x06000035 RID: 53 RVA: 0x000034E4 File Offset: 0x00001AE4
		public void WriteAnsiString(string str, Encoding encoding)
		{
			byte[] bytes = encoding.GetBytes(str);
			this._stream.Write(bytes, 0, bytes.Length);
		}

		// Token: 0x06000036 RID: 54 RVA: 0x00003509 File Offset: 0x00001B09
		public void WriteAnsiString(string str, int codePage = 1251)
		{
			this.WriteAnsiString(str, Encoding.GetEncoding(codePage));
		}

		// Token: 0x06000037 RID: 55 RVA: 0x00003518 File Offset: 0x00001B18
		public void WriteAnsiStringFixedLength(string str, int fixedLength, Encoding encoding, byte nullableValue = 0)
		{
			byte[] bytes = encoding.GetBytes(str);
			if (bytes.Length > fixedLength)
			{
				this._stream.Write(bytes, 0, fixedLength);
				return;
			}
			this._stream.Write(bytes, 0, bytes.Length);
			int count = fixedLength - bytes.Length;
			this.WriteRepeatByte(nullableValue, count);
		}

		// Token: 0x06000038 RID: 56 RVA: 0x00003561 File Offset: 0x00001B61
		public void WriteAnsiStringFixedLength(string str, int fixedLength, byte nullableValue = 0, int codePage = 1251)
		{
			this.WriteAnsiStringFixedLength(str, fixedLength, Encoding.GetEncoding(codePage), nullableValue);
		}

		// Token: 0x06000039 RID: 57 RVA: 0x00003573 File Offset: 0x00001B73
		public void WriteAnsiStringWithStopByte(string str, Encoding encoding, byte stopByte = 0)
		{
			this.WriteAnsiString(str, encoding);
			this.WriteByte(stopByte);
		}

		// Token: 0x0600003A RID: 58 RVA: 0x00003584 File Offset: 0x00001B84
		public void WriteAnsiStringWithStopByte(string str, byte stopByte = 0, int codePage = 1252)
		{
			this.WriteAnsiStringWithStopByte(str, Encoding.GetEncoding(codePage), stopByte);
		}

		// Token: 0x0600003B RID: 59 RVA: 0x00003594 File Offset: 0x00001B94
		public string ReadUnicodeStringWithStopWord(ushort stopWord = 0)
		{
			int num = 0;
			long position = this._stream.Position;
			while (this.ReadUInt16(ByteEncoding.None) != stopWord)
			{
				num += 2;
			}
			this.Position = position;
			Encoding encoding = Encoding.Unicode;
			if (this.SelectedByteEncoding == ByteEncoding.Big)
			{
				encoding = Encoding.BigEndianUnicode;
			}
			byte[] bytes = this.ReadByteArray(num);
			this.Position += 2L;
			return encoding.GetString(bytes);
		}

		// Token: 0x0600003C RID: 60 RVA: 0x000035FC File Offset: 0x00001BFC
		public void WriteUnicodeStringWithStopWord(string str, ushort stopWord = 0)
		{
			Encoding encoding = Encoding.Unicode;
			if (this.SelectedByteEncoding == ByteEncoding.Big)
			{
				encoding = Encoding.BigEndianUnicode;
			}
			this.WriteAnsiString(str, encoding);
			this.WriteUInt16(stopWord, ByteEncoding.None);
		}

		// Token: 0x0600003D RID: 61 RVA: 0x00003630 File Offset: 0x00001C30
		public void AlignPosition(int value)
		{
			while (this._stream.Position % (long)value != 0L)
			{
				Stream stream = this._stream;
				long position = stream.Position;
				stream.Position = position + 1L;
			}
		}

		// Token: 0x0600003E RID: 62 RVA: 0x00003665 File Offset: 0x00001C65
		public void AlignPositionWithByte(int value, byte alignByte = 0)
		{
			while (this._stream.Position % (long)value != 0L)
			{
				this._stream.WriteByte(alignByte);
			}
		}

		// Token: 0x0600003F RID: 63 RVA: 0x00003688 File Offset: 0x00001C88
		public byte[] GetStreamBytes()
		{
			long position = this.Position;
			this.Position = 0L;
			byte[] result = this.ReadByteArray((int)this.Length);
			this.Position = position;
			return result;
		}

		// Token: 0x06000040 RID: 64 RVA: 0x000036B8 File Offset: 0x00001CB8
		public static StreamHelper CreateFromFileInMemory(string fileName)
		{
			StreamHelper streamHelper = new StreamHelper(ByteEncoding.Little);
			using (FileStream fileStream = new FileStream(fileName, FileMode.Open, FileAccess.Read, FileShare.Read))
			{
				fileStream.CopyTo(streamHelper.Stream);
			}
			streamHelper.Position = 0L;
			return streamHelper;
		}

		// Token: 0x06000041 RID: 65 RVA: 0x00003708 File Offset: 0x00001D08
		public void SaveToFile(string fileName, bool removeIfExist = false)
		{
			if (removeIfExist && File.Exists(fileName))
			{
				File.Delete(fileName);
			}
			using (FileStream fileStream = new FileStream(fileName, FileMode.OpenOrCreate, FileAccess.ReadWrite))
			{
				this._stream.Position = 0L;
				this._stream.CopyTo(fileStream, 4096);
			}
			this.Position = 0L;
		}

		// Token: 0x04000005 RID: 5
		private Stream _stream;

		// Token: 0x04000006 RID: 6
		private Type _streamType;

		// Token: 0x04000007 RID: 7
		private ByteEncoding _byteEncoding;
	}
}
