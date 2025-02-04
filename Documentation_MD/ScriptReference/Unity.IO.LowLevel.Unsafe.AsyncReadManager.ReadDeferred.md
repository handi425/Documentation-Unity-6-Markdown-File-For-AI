[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#
[AsyncReadManager](Unity.IO.LowLevel.Unsafe.AsyncReadManager.html).ReadDeferred

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

## Declaration

public static
[Unity.IO.LowLevel.Unsafe.ReadHandle](Unity.IO.LowLevel.Unsafe.ReadHandle.html)
ReadDeferred(ref
[Unity.IO.LowLevel.Unsafe.FileHandle](Unity.IO.LowLevel.Unsafe.FileHandle.html)
fileHandle, ReadCommandArray* readCmdArray,
[Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html) dependency);

### Parameters

fileHandle | The FileHandle to be read from, opened by [AsyncReadManager.OpenFileAsync](Unity.IO.LowLevel.Unsafe.AsyncReadManager.OpenFileAsync.html).  
---|---  
readCmdArray | A pointer to a struct containing the read commands to queue.  
dependency | The dependency that will trigger the read to begin.  
  
### Returns

**ReadHandle** A [ReadHandle](Unity.IO.LowLevel.Unsafe.ReadHandle.html) object
you can to use to check the status and monitor the progress of the read
operations.

### Description

Queues a set of read operations for a file once the specified Jobs have
completed.

This function does not make a copy of the
[ReadCommandArray](Unity.IO.LowLevel.Unsafe.ReadCommandArray.html) struct
passed as a parameter. You can change the read commands until the Jobs passed
to this function as a dependency are complete. The read will automatically
wait for the
[FileHandle.JobHandle](Unity.IO.LowLevel.Unsafe.FileHandle.JobHandle.html) to
be complete.  
  
As an unsafe, low-level API, it is the user's responsibility to avoid changing
or freeing the
[ReadCommandArray](Unity.IO.LowLevel.Unsafe.ReadCommandArray.html) after the
read operation has started. Doing so could lead to buffer overruns and race
conditions. (If you change the number of commands, remember to update the
[ReadCommandArray.CommandCount](Unity.IO.LowLevel.Unsafe.ReadCommandArray.CommandCount.html)
field, too.)  
  
**Note:** WebGL builds do not support using `AsyncReadManager` to open files
from a remote web server; for example, from the path
`Application.streamingAssetsPath` which maps to a URL on a remote web server.

    
    
    using System.IO;
    using Unity.Collections;
    using Unity.IO.LowLevel.Unsafe;
    using Unity.Collections.LowLevel.Unsafe;
    using UnityEngine;
    using Unity.Jobs;  
      
    class AsyncReadSample : [MonoBehaviour](MonoBehaviour.html)
    {
        static string TestFilename = Path.Combine([Application.streamingAssetsPath](Application-streamingAssetsPath.html), "myfile.bin");  
      
        public unsafe struct ReadCommandJob : [IJob](Unity.Jobs.IJob.html)
        {
            public NativeArray<[ReadCommandArray](Unity.IO.LowLevel.Unsafe.ReadCommandArray.html)> ReadCmdArrayNative;  
      
            public void Execute()
            {
                const int kReadCount = 1;
                const int kReadSize = 2048;  
      
                [ReadCommand](Unity.IO.LowLevel.Unsafe.ReadCommand.html)* readCmds = ([ReadCommand](Unity.IO.LowLevel.Unsafe.ReadCommand.html)*)[UnsafeUtility.Malloc](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.Malloc.html)(sizeof([ReadCommand](Unity.IO.LowLevel.Unsafe.ReadCommand.html)) * kReadCount, 16, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));  
      
                readCmds[0] = new [ReadCommand](Unity.IO.LowLevel.Unsafe.ReadCommand.html)()
                {
                    Buffer = (byte*)[UnsafeUtility.Malloc](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.Malloc.html)(kReadSize, 16, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html)),
                    Offset = 0,
                    Size = kReadSize
                };  
      
                ReadCmdArrayNative[0] = new [ReadCommandArray](Unity.IO.LowLevel.Unsafe.ReadCommandArray.html)
                {
                    ReadCommands = readCmds,
                    CommandCount = kReadCount
                };
            }
        }  
      
        public unsafe void SetupReadInJob()
        {
            NativeArray<[ReadCommandArray](Unity.IO.LowLevel.Unsafe.ReadCommandArray.html)> readCmdArrayNative = new NativeArray<[ReadCommandArray](Unity.IO.LowLevel.Unsafe.ReadCommandArray.html)>(1, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
            [ReadCommandArray](Unity.IO.LowLevel.Unsafe.ReadCommandArray.html)* readCmdArrayPtr = ([ReadCommandArray](Unity.IO.LowLevel.Unsafe.ReadCommandArray.html)*)readCmdArrayNative.GetUnsafePtr();  
      
            [FileHandle](Unity.IO.LowLevel.Unsafe.FileHandle.html) fileHandle = [AsyncReadManager.OpenFileAsync](Unity.IO.LowLevel.Unsafe.AsyncReadManager.OpenFileAsync.html)(TestFilename);  
      
            var createReadCommandJob = new ReadCommandJob
            {
                ReadCmdArrayNative = readCmdArrayNative
            }.Schedule();  
      
            [ReadHandle](Unity.IO.LowLevel.Unsafe.ReadHandle.html) readHandle = [AsyncReadManager.ReadDeferred](Unity.IO.LowLevel.Unsafe.AsyncReadManager.ReadDeferred.html)(fileHandle, readCmdArrayPtr, createReadCommandJob);  
      
            [JobHandle](Unity.Jobs.JobHandle.html) closeJob = fileHandle.Close(readHandle.JobHandle);  
      
            createReadCommandJob.Complete(); // Ensure the NativeArray is finished with before using
            closeJob.Complete();  
      
            // ... Use the data read into the buffer  
      
            readHandle.Dispose();  
      
            for (int i = 0; i < readCmdArrayNative[0].CommandCount; i++)
                [UnsafeUtility.Free](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.Free.html)(readCmdArrayNative[0].ReadCommands[i].Buffer, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
            [UnsafeUtility.Free](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.Free.html)(readCmdArrayNative[0].ReadCommands, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));  
      
            readCmdArrayNative.Dispose();
        }
    }
    

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

