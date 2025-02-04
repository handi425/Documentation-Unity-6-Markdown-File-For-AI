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

# CaptureFlags

enumeration

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

Flags that specify what kind of data to capture in a snapshot.

These flags provide control for what broad data categories should be included
in the snapshot. For general purpose captures it is recommended to capture
with all flags, or at least with
[CaptureFlags.ManagedObjects](Unity.Profiling.Memory.CaptureFlags.ManagedObjects.html),
[CaptureFlags.NativeObjects](Unity.Profiling.Memory.CaptureFlags.NativeObjects.html)
and
[CaptureFlags.NativeAllocations](Unity.Profiling.Memory.CaptureFlags.NativeAllocations.html).  
  
For more focused investigations where the size of the snapshot and the speed
at which it is taken are important, you can use a narrower set of
[CaptureFlags](Unity.Profiling.Memory.CaptureFlags.html). For example, if the
only goal is to check native object sizes, then not setting the
[CaptureFlags.ManagedObjects](Unity.Profiling.Memory.CaptureFlags.ManagedObjects.html)
flag can greately reduce capture time and size. If detailed NativeAllocations,
such as those used by native collections, and the graphics sizes of native
objects is not important, the
[CaptureFlags.NativeAllocations](Unity.Profiling.Memory.CaptureFlags.NativeAllocations.html)
can be left off as well.  
  
**Note:**
[CaptureFlags.NativeAllocations](Unity.Profiling.Memory.CaptureFlags.NativeAllocations.html)
and
[CaptureFlags.NativeAllocationSites](Unity.Profiling.Memory.CaptureFlags.NativeAllocationSites.html)
won't add extra data to the snapshot unless the build supports the collection
of native call stack information, which currently requires source code access.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections;
    using System.IO;
    using Unity.Profiling.Memory;
    using UnityEngine;  
      
    public static class MemoryProfilerExample
    {
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
[MemoryProfiler.TakeSnapshot](Unity.Profiling.Memory.MemoryProfiler.TakeSnapshot.html).

### Properties

[ManagedObjects](Unity.Profiling.Memory.CaptureFlags.ManagedObjects.html)|
Specifies that the entire managed heap and all the data needed to parse it
should be captured as part of the Memory Snapshot.  
---|---  
[NativeObjects](Unity.Profiling.Memory.CaptureFlags.NativeObjects.html)|
Specifies that information about Native Objects should be collected.  
[NativeAllocations](Unity.Profiling.Memory.CaptureFlags.NativeAllocations.html)|
Specifies that the Native Memory used by any Native Allocation made by Unity
should be captured.  
[NativeAllocationSites](Unity.Profiling.Memory.CaptureFlags.NativeAllocationSites.html)|
Specifies the location that each native allocation was allocated at.  
[NativeStackTraces](Unity.Profiling.Memory.CaptureFlags.NativeStackTraces.html)|
Specifies that Call-Stack Symbols for the Native Call-stack of each Allocation
should be collected.  
  
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

