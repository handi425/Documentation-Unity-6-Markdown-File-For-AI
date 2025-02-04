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

# MemoryProfiler

class in Unity.Profiling.Memory

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

### Description

The memory profiler API provides functionality for taking memory snapshots or
adding metadata to them.

The API is available at runtime. When you call this API to take snapshots, it
stores the snapshots locally on the storage of the device the Player is
running on, or stream it out if the Unity Editor is attached via
[PlayerConnection](Networking.PlayerConnection.PlayerConnection.html). When
called from within the Editor, it captures data from the Editor or an attached
Player, depending on the current target of the PlayerConnection. You can also
set the current target of the Player Connection via the Editor through the
[Profiler Window](../Manual/ProfilerWindow.html), the [Memory
Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest/)
or the [Console Window](../Manual/Console.html). You can open the resulting
snapshot files with the [Memory
Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest/),
if they are saved with the `.snap` file extension.  
  
Listeners of the
[MemoryProfiler.CreatingMetadata](Unity.Profiling.Memory.MemoryProfiler.CreatingMetadata.html)
event will only be notified on the Player or Editor where the snapshot is
being taken from.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections;
    using System.IO;
    using Unity.Profiling.Memory;
    using UnityEngine;  
      
    public static class MemoryProfilerExample
    {
        [RuntimeInitializeOnLoadMethod]
        public static void Initialize()
        {
            [MemoryProfiler.CreatingMetadata](Unity.Profiling.Memory.MemoryProfiler.CreatingMetadata.html) += CreateMetadata;
        }  
      
        static void CreateMetadata([MemorySnapshotMetadata](Unity.Profiling.Memory.MemorySnapshotMetadata.html) metadata)
        {
            metadata.Description = $"This Memory Snapshot capture started at {DateTime.Now}.";
        }  
      
        public static IEnumerator TakeSnapshot()
        {
            var snapshotFileName = "SnapshotName.tmpsnap";
            // Make sure the file does not exist, e.g. as a left over of a failed previous attempt to take a snapshot.
            if ([File.Exists](Windows.File.Exists.html)(snapshotFileName))
                [File.Delete](Windows.File.Delete.html)(snapshotFileName);  
      
            bool snapshotFinished = false;
            string resultingSnapshotPath = null;
            [MemoryProfiler.TakeSnapshot](Unity.Profiling.Memory.MemoryProfiler.TakeSnapshot.html)(snapshotFileName, (filePath, success) =>
            {
                snapshotFinished = true;
                if (success)
                {
                    resultingSnapshotPath = Path.GetFullPath(filePath);
                    [Debug.Log](Debug.Log.html)($"Snapshot captured and stored at {resultingSnapshotPath}.");
                }
                else
                {
                    [Debug.LogError](Debug.LogError.html)("Failed to take a snapshot.");
                }
            },
                [CaptureFlags.ManagedObjects](Unity.Profiling.Memory.CaptureFlags.ManagedObjects.html) | [CaptureFlags.NativeObjects](Unity.Profiling.Memory.CaptureFlags.NativeObjects.html) | [CaptureFlags.NativeAllocations](Unity.Profiling.Memory.CaptureFlags.NativeAllocations.html));  
      
            while (!snapshotFinished)
            {
                yield return null;
            }  
      
            if (resultingSnapshotPath != null && [File.Exists](Windows.File.Exists.html)(resultingSnapshotPath))
            {
                var finalPath = resultingSnapshotPath.Replace(".tmpsnap", ".snap");
                // Remove any pre-existing file first.
                if ([File.Exists](Windows.File.Exists.html)(finalPath))
                    [File.Delete](Windows.File.Delete.html)(finalPath);  
      
                // Now that writing to the file has succesfully completed, rename the file to the .snap extension to denote that the Memory [Profiler](Profiling.Profiler.html) can open it.
                File.Move(resultingSnapshotPath, finalPath);  
      
                // If you don't have access to the Player's file system you could also upload the file to an end-point that is accessible to you here.
            }
        }
    }
    

Additional resources: [Memory Profiler
package](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest/),
[PlayerConnection](Networking.PlayerConnection.PlayerConnection.html),
[EditorConnection](Networking.PlayerConnection.EditorConnection.html),
[PlayerConnectionGUIUtility](Networking.PlayerConnection.PlayerConnectionGUIUtility.html).

### Static Methods

[TakeSnapshot](Unity.Profiling.Memory.MemoryProfiler.TakeSnapshot.html)|
Triggers a memory snapshot capture to generate a capture of the memory state
that the Memory Profiler can open and analyze.  
---|---  
[TakeTempSnapshot](Unity.Profiling.Memory.MemoryProfiler.TakeTempSnapshot.html)|
Triggers a memory snapshot capture to the Application.temporaryCachePath
folder.  
  
### Events

[CreatingMetadata](Unity.Profiling.Memory.MemoryProfiler.CreatingMetadata.html)|
A metadata event that collection methods can subscribe to.  
---|---  
  
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

