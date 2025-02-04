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
[MemoryProfiler](Unity.Profiling.Memory.MemoryProfiler.html).CreatingMetadata

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

A metadata event that collection methods can subscribe to.

This event is fired when you capture a memory snapshot. Use it to provide meta
data to the snapshot file, for example information related to the context,
such as the level, in which it was taken.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using UnityEngine;
    using Unity.Profiling.Memory;  
      
    public class MemoryProfilerExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public string levelName = "Default Level Name";  
      
        void Start()
        {
            [MemoryProfiler.CreatingMetadata](Unity.Profiling.Memory.MemoryProfiler.CreatingMetadata.html) += CreateMetadata;
        }  
      
        void CreateMetadata([MemorySnapshotMetadata](Unity.Profiling.Memory.MemorySnapshotMetadata.html) metadata)
        {
            metadata.Description = $"This Memory Snapshot capture started at {DateTime.Now} in level {levelName}.";
        }  
      
        void OnDestroy()
        {
            [MemoryProfiler.CreatingMetadata](Unity.Profiling.Memory.MemoryProfiler.CreatingMetadata.html) -= CreateMetadata;
        }
    }
    

**Note:** If the project has the [Memory Profiler
package](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest/)
installed in the Editor, it is recommended to implement a concrete
implementation of
[MemoryProfiler.MetadataCollect](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest/index.html?subfolder=/api/Unity.MemoryProfiler.MetadataCollect.html)
instead, which will inject your implementation into any Player builds you
make.  
  
Additional resources:
[MemoryProfiler.MetadataCollect](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest/index.html?subfolder=/api/Unity.MemoryProfiler.MetadataCollect.html),
[MemoryProfiler.TakeSnapshot](Unity.Profiling.Memory.MemoryProfiler.TakeSnapshot.html),
[MemorySnapshotMetadata](Unity.Profiling.Memory.MemorySnapshotMetadata.html).

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

