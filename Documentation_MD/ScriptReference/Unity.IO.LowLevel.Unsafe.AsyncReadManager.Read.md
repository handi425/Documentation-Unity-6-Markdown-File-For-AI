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

#  [AsyncReadManager](Unity.IO.LowLevel.Unsafe.AsyncReadManager.html).Read

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
Read(string filename, ReadCommand* readCmds, uint readCmdCount, string
assetName, ulong typeID,
[Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem](Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.html)
subsystem);

### Parameters

filename | The filename to read from.  
---|---  
readCmds | A pointer to an array of ReadCommand structs that specify offset, size, and destination buffer.  
readCmdCount | The number of read commands pointed to by readCmds.  
assetName | (Optional) The name of the object being read, for metrics purposes.  
typeID | (Optional) The [TypeID](../Manual/ClassIDReference.html) of the object being read, for metrics purposes.  
subsystem | (Optional) The [Subsystem tag](Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.html) for the read operation, for metrics purposes.  
  
### Returns

**ReadHandle** Used to monitor the progress and status of the read command.

### Description

Issues an asynchronous file read operation. Returns a ReadHandle.

You can set the `assetName`, `typeId`, and `subsystem` parameters to collect
asset-specific metrics for this read operation. When you enable metrics
collection with
[AsyncReadManagerMetrics.StartCollectingMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.StartCollectingMetrics.html),
Unity includes this information as part of the
[AsyncReadManagerMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.html),
allowing you to analyze how different types of assets affect performance.

The AsyncReadManager copies the data referenced by `Read`; you can dispose or
free the data immediately after calling `Read`.

    
    
    using System.IO;
    using Unity.Collections;
    using Unity.IO.LowLevel.Unsafe;
    using Unity.Collections.LowLevel.Unsafe;
    using UnityEngine;  
      
    class AsyncReadSample : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ReadHandle](Unity.IO.LowLevel.Unsafe.ReadHandle.html) readHandle;
        NativeArray<[ReadCommand](Unity.IO.LowLevel.Unsafe.ReadCommand.html)> cmds;
        string assetName = "myfile";
        ulong typeID = 114; // from [ClassIDReference](../Manual/ClassIDReference.html)
        [AssetLoadingSubsystem](Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.html) subsystem = [AssetLoadingSubsystem.Scripts](Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.Scripts.html);  
      
        public unsafe void Start()
        {
            string filePath = Path.Combine([Application.streamingAssetsPath](Application-streamingAssetsPath.html), "myfile.bin");
            cmds = new NativeArray<[ReadCommand](Unity.IO.LowLevel.Unsafe.ReadCommand.html)>(1, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
            [ReadCommand](Unity.IO.LowLevel.Unsafe.ReadCommand.html) cmd;
            cmd.Offset = 0;
            cmd.Size = 1024;
            cmd.Buffer = (byte*)[UnsafeUtility.Malloc](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.Malloc.html)(cmd.Size, 16, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
            cmds[0] = cmd;
            readHandle = [AsyncReadManager.Read](Unity.IO.LowLevel.Unsafe.AsyncReadManager.Read.html)(filePath, ([ReadCommand](Unity.IO.LowLevel.Unsafe.ReadCommand.html)*)cmds.GetUnsafePtr(), 1, assetName, typeID, subsystem);
        }  
      
        public unsafe void [Update](PlayerLoop.Update.html)()
        {
            if (readHandle.IsValid() && readHandle.Status != [ReadStatus.InProgress](Unity.IO.LowLevel.Unsafe.ReadStatus.InProgress.html))
            {
                [Debug.LogFormat](Debug.LogFormat.html)("Read {0}", readHandle.Status == [ReadStatus.Complete](Unity.IO.LowLevel.Unsafe.ReadStatus.Complete.html) ? "Successful" : "Failed");
                readHandle.Dispose();
                [UnsafeUtility.Free](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.Free.html)(cmds[0].Buffer, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
                cmds.Dispose();
            }
        }
    }
    

* * *

## Declaration

public static
[Unity.IO.LowLevel.Unsafe.ReadHandle](Unity.IO.LowLevel.Unsafe.ReadHandle.html)
Read(ref
[Unity.IO.LowLevel.Unsafe.FileHandle](Unity.IO.LowLevel.Unsafe.FileHandle.html)
fileHandle,
[Unity.IO.LowLevel.Unsafe.ReadCommandArray](Unity.IO.LowLevel.Unsafe.ReadCommandArray.html)
readCmdArray);

### Parameters

fileHandle | The FileHandle to be read from, opened by [AsyncReadManager.OpenFileAsync](Unity.IO.LowLevel.Unsafe.AsyncReadManager.OpenFileAsync.html).  
---|---  
readCmdArray | A struct containing the read commands to queue.  
  
### Returns

**ReadHandle** A [ReadHandle](Unity.IO.LowLevel.Unsafe.ReadHandle.html) object
you can use to check the status and monitor the progress of the read
operations.

### Description

Queues a set of read operations for a file opened with
[OpenFileAsync](Unity.IO.LowLevel.Unsafe.AsyncReadManager.OpenFileAsync.html).

This function makes a copy of the
[ReadCommandArray](Unity.IO.LowLevel.Unsafe.ReadCommandArray.html) struct
passed as a parameter internally, so you do not need to maintain the array.
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
      
        public unsafe void Start()
        {
            [ReadCommand](Unity.IO.LowLevel.Unsafe.ReadCommand.html) cmd;
            cmd.Offset = 0;
            cmd.Size = 1024;
            cmd.Buffer = (byte*)[UnsafeUtility.Malloc](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.Malloc.html)(cmd.Size, 16, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));  
      
            [FileHandle](Unity.IO.LowLevel.Unsafe.FileHandle.html) fileHandle = [AsyncReadManager.OpenFileAsync](Unity.IO.LowLevel.Unsafe.AsyncReadManager.OpenFileAsync.html)(TestFilename);  
      
            [ReadCommandArray](Unity.IO.LowLevel.Unsafe.ReadCommandArray.html) readCmdArray;
            readCmdArray.ReadCommands = &cmd;
            readCmdArray.CommandCount = 1;  
      
            [ReadHandle](Unity.IO.LowLevel.Unsafe.ReadHandle.html) readHandle = [AsyncReadManager.Read](Unity.IO.LowLevel.Unsafe.AsyncReadManager.Read.html)(fileHandle, readCmdArray);  
      
            [JobHandle](Unity.Jobs.JobHandle.html) closeJob = fileHandle.Close(readHandle.JobHandle);  
      
            closeJob.Complete();  
      
            // ... Use the data read into the buffer  
      
            readHandle.Dispose();  
      
            for (int i = 0; i < readCmdArray.CommandCount; i++)
                [UnsafeUtility.Free](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.Free.html)(readCmdArray.ReadCommands[i].Buffer, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
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

