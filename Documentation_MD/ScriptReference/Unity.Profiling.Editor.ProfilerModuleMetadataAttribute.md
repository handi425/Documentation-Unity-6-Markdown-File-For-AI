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

# ProfilerModuleMetadataAttribute

class in Unity.Profiling.Editor

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

Provides metadata related to a
[ProfilerModule](Unity.Profiling.Editor.ProfilerModule.html), such as its name
and icon path.

You must attribute a
[ProfilerModule](Unity.Profiling.Editor.ProfilerModule.html) derived type with
[ProfilerModuleMetadataAttribute](Unity.Profiling.Editor.ProfilerModuleMetadataAttribute.html)
for Unity to display it in the Profiler window.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using Unity.Profiling;
    using Unity.Profiling.Editor;  
      
    [Serializable]
    [ProfilerModuleMetadata("Garbage Collection")]
    public class GarbageCollectionProfilerModule : [ProfilerModule](Unity.Profiling.Editor.ProfilerModule.html)
    {
        static readonly [ProfilerCounterDescriptor](Unity.Profiling.Editor.ProfilerCounterDescriptor.html)[] k_ChartCounters = new [ProfilerCounterDescriptor](Unity.Profiling.Editor.ProfilerCounterDescriptor.html)[]
        {
            new [ProfilerCounterDescriptor](Unity.Profiling.Editor.ProfilerCounterDescriptor.html)("GC Reserved Memory", [ProfilerCategory.Memory](Unity.Profiling.ProfilerCategory.Memory.html)),
            new [ProfilerCounterDescriptor](Unity.Profiling.Editor.ProfilerCounterDescriptor.html)("GC Used Memory", [ProfilerCategory.Memory](Unity.Profiling.ProfilerCategory.Memory.html)),
            new [ProfilerCounterDescriptor](Unity.Profiling.Editor.ProfilerCounterDescriptor.html)("GC Allocated In Frame", [ProfilerCategory.Memory](Unity.Profiling.ProfilerCategory.Memory.html)),
        };  
      
        public GarbageCollectionProfilerModule() : base(k_ChartCounters) {}
    }
    

Additional resources:
[ProfilerModule](Unity.Profiling.Editor.ProfilerModule.html).

### Properties

[DisplayName](Unity.Profiling.Editor.ProfilerModuleMetadataAttribute.DisplayName.html)|
The attributed Profiler module’s display name.  
---|---  
[IconPath](Unity.Profiling.Editor.ProfilerModuleMetadataAttribute.IconPath.html)|
The path to the attributed Profiler module’s icon.  
  
### Constructors

[ProfilerModuleMetadataAttribute](Unity.Profiling.Editor.ProfilerModuleMetadataAttribute-
ctor.html)| Initializes and returns an instance of
ProfilerModuleMetadataAttribute.  
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

