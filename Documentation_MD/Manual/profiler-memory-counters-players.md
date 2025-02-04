[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/profiler-memory-counters-players.html)
  * [中文](/cn/current/Manual/profiler-memory-counters-players.html)
  * [日本語](/ja/current/Manual/profiler-memory-counters-players.html)
  * [한국어](/kr/current/Manual/profiler-memory-counters-players.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/profiler-memory-counters-players.html)
  * [中文](/cn/current/Manual/profiler-memory-counters-players.html)
  * [日本語](/ja/current/Manual/profiler-memory-counters-players.html)
  * [한국어](/kr/current/Manual/profiler-memory-counters-players.html)

  * [Optimization](analysis.html)
  * [Unity Profiler](Profiler.html)
  * [Collect performance data](profiler-collect-data.html)
  * [Memory performance data](profiler-memory.html)
  * Accessing memory counters in players

[](profiler-memory-introduction.html)

Memory Profiler module introduction

[](ProfilerMemory.html)

Memory Profiler module reference

# Accessing memory counters in players

You can use the [ProfilerRecorder
API](../ScriptReference/Unity.Profiling.ProfilerRecorder.html) to access the
Memory **Profiler** A window that helps you to optimize your game. It shows
how much time is spent in the various areas of your game. For example, it can
report the percentage of time spent rendering, animating, or in your game
logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) module’s counters in a player.

The following example contains a simple script that collects **Total Reserved
Memory** , **GC Reserved Memory** and **System Used Memory** metrics, and
displays those as a [`GUI.TextArea`](../ScriptReference/GUI.TextArea.html).
The Memory Profiler module information belongs to the
[`ProfilerCategory.Memory`](../ScriptReference/Unity.Profiling.ProfilerCategory.Memory.html)
**Profiler category** Identifies the workload data for a Unity subsystem (for
example, Rendering, Scripting and Animation categories). Unity applies color-
coding to categories to visually distinguish between the types of data in the
**Profiler** window.  
See in [Glossary](Glossary.html#Profilercategory).

    
    
    using System.Text;
    using Unity.Profiling;
    using UnityEngine;
    
    public class MemoryStatsScript : MonoBehaviour
    {
        string statsText;
        ProfilerRecorder totalReservedMemoryRecorder;
        ProfilerRecorder gcReservedMemoryRecorder;
        ProfilerRecorder systemUsedMemoryRecorder;
    
        void OnEnable()
        {
            totalReservedMemoryRecorder = ProfilerRecorder.StartNew(ProfilerCategory.Memory, "Total Reserved Memory");
            gcReservedMemoryRecorder = ProfilerRecorder.StartNew(ProfilerCategory.Memory, "GC Reserved Memory");
            systemUsedMemoryRecorder = ProfilerRecorder.StartNew(ProfilerCategory.Memory, "System Used Memory");
        }
    
        void OnDisable()
        {
            totalReservedMemoryRecorder.Dispose();
            gcReservedMemoryRecorder.Dispose();
            systemUsedMemoryRecorder.Dispose();
        }
    
        void Update()
        {
            var sb = new StringBuilder(500);
            if (totalReservedMemoryRecorder.Valid)
                sb.AppendLine($"Total Reserved Memory: {totalReservedMemoryRecorder.LastValue}");
            if (gcReservedMemoryRecorder.Valid)
                sb.AppendLine($"GC Reserved Memory: {gcReservedMemoryRecorder.LastValue}");
            if (systemUsedMemoryRecorder.Valid)
                sb.AppendLine($"System Used Memory: {systemUsedMemoryRecorder.LastValue}");
            statsText = sb.ToString();
        }
    
        void OnGUI()
        {
            GUI.TextArea(new Rect(10, 30, 250, 50), statsText);
        }
    }
    

The following screenshot shows the result of adding the script to the [Tanks!
tutorial project](https://assetstore.unity.com/packages/essentials/tutorial-
projects/tanks-tutorial-46209).

![Tanks! tutorial with the overlaid memory
information](../uploads/Main/profiler-tanks-memory-overlay.png) Tanks!
tutorial with the overlaid memory information

This information is available in release players, as are the other [high level
counters available in the Memory Profiler module](ProfilerMemory.html). If you
want to view the selected memory counters in a custom module in the Profiler
window, use the [Profiler module editor](profiler-module-editor.html) to
configure the chart.

For more information on adding profiler information to your code, refer to
[Adding profiling information to your code](profiler-adding-information-
code.html).

## Additional resources

  * [Adding profiling information to your code](profiler-adding-information-code.html)
  * [Visualizing profiler counters](profiler-creating-custom-counters.html)
  * [Memory Profiler module reference](ProfilerMemory.html)
  * [Memory Profiler module introduction](profiler-memory-introduction.html)

[](profiler-memory-introduction.html)

Memory Profiler module introduction

[](ProfilerMemory.html)

Memory Profiler module reference

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

