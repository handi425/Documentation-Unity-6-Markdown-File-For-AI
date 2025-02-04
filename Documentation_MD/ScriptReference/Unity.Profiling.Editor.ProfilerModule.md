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

# ProfilerModule

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

Represents a Profiler module in the Profiler window.

Use ProfilerModule to extend the Profiler window with custom Profiler modules.
You can use ProfilerModule with the [Profiling Core
package](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest),
to expose and visualize performance metrics for your own systems in the
Profiler window.  
  
To define a [ProfilerModule](Unity.Profiling.Editor.ProfilerModule.html)
derived type, use an [Editor script](../Manual/SpecialFolders.html) inside
your project or package and attribute it with the
[ProfilerModuleMetadataAttribute](Unity.Profiling.Editor.ProfilerModuleMetadataAttribute.html).
At a minimum, you must define the Profiler module’s name and chart counters,
as shown below. The Profiler window automatically displays any
[ProfilerModule](Unity.Profiling.Editor.ProfilerModule.html) derived types
present in your project.

    
    
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
      
        public GarbageCollectionProfilerModule() : base(k_ChartCounters) { }
    }
    

When a Profiler module is selected in the Profiler window, Unity displays the
module's **Details View** , which contains additional, relevant performance
data. By default, a module’s **Details View** displays a list of its chart’s
counters alongside their current values in the selected frame. You can
implement a custom **Details View** to present a bespoke visualization of your
performance data when the module is selected. For more information, see
[ProfilerModule.CreateDetailsViewController](Unity.Profiling.Editor.ProfilerModule.CreateDetailsViewController.html).  
  
Additional resources:
[ProfilerModuleMetadataAttribute](Unity.Profiling.Editor.ProfilerModuleMetadataAttribute.html),
[ProfilerCounterDescriptor](Unity.Profiling.Editor.ProfilerCounterDescriptor.html),
[ProfilerModuleChartType](Unity.Profiling.Editor.ProfilerModuleChartType.html),
[ProfilerModuleViewController](Unity.Profiling.Editor.ProfilerModuleViewController.html).

### Properties

[DisplayName](Unity.Profiling.Editor.ProfilerModule.DisplayName.html)| The
module’s display name.  
---|---  
[ProfilerWindow](Unity.Profiling.Editor.ProfilerModule.ProfilerWindow.html)|
The Profiler window that the module instance belongs to.  
  
### Public Methods

[CreateDetailsViewController](Unity.Profiling.Editor.ProfilerModule.CreateDetailsViewController.html)|
Creates a View Controller object that draws the Profiler module’s Details View
in the Profiler window. Unity calls this method automatically when the module
is selected in the Profiler window.  
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

