[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/frame-timing-manager-get-timing-data.html)
  * [中文](/cn/current/Manual/frame-timing-manager-get-timing-data.html)
  * [日本語](/ja/current/Manual/frame-timing-manager-get-timing-data.html)
  * [한국어](/kr/current/Manual/frame-timing-manager-get-timing-data.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/frame-timing-manager-get-timing-data.html)
  * [中文](/cn/current/Manual/frame-timing-manager-get-timing-data.html)
  * [日本語](/ja/current/Manual/frame-timing-manager-get-timing-data.html)
  * [한국어](/kr/current/Manual/frame-timing-manager-get-timing-data.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Profile rendering](profile-rendering.html)
  * [Frame Timing Manager](frame-timing-manager-landing.html)
  * Get frame timing data

[](frame-timing-manager-enable.html)

Enable the FrameTimingManager

[](frame-timing-manager-record-timing-data.html)

Record frame timing data

# Get frame timing data

## View frame time data with a Custom Profiler module

To view frame timing data in a Custom **Profiler** A window that helps you to
optimize your game. It shows how much time is spent in the various areas of
your game. For example, it can report the percentage of time spent rendering,
animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) module:

  1. Create a custom profiler module according to the instructions on [Creating a custom profiler module](profiler-module-editor.html).
  2. In the **Profiler Module Editor** window, select your custom module.
  3. In the **Available Counters** panel, select **Unity**.
  4. Select **Render** to open the submenu that contains **profiler counters** Placed in code with the ProfilerCounter API to track metrics, such as the number of enemies spawned in your game. [More info](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilercounter-guide.html)  
See in [Glossary](Glossary.html#Profilercounter) related to memory usage,
which includes those that the **FrameTimingStats** property enables. You can
then click on the relevant counters in the submenu to add them to your custom
module.

The following table describes the purpose of each of the counters that become
available when you enable **Frame Timing Stats** :

**Measurement** | **Description**  
---|---  
**CPU Total Frame Time (ms)** | The total CPU frame time, in milliseconds. Unity calculates this as the time between the ends of two frames, including any overheads or time spent waiting in between frames.  
**CPU Main Thread Frame Time (ms)** | The time between the start of the frame and the time when the Main Thread finished the work it performed during that frame, in milliseconds.  
**CPU Main Thread Present Wait Time (ms)** | The CPU time spent waiting for Present() during the frame.  
**CPU Render Thread Frame Time (ms)** | The time between the start of the work on the Render Thread and when Unity calls the Present() function, in milliseconds.  
**GPU Frame Time (ms)** | The time difference between the beginning and the end of the GPU rendering a single frame, in milliseconds.  
  
## Retrieve timestamp data from the FrameTimingManager C# API

Use the FrameTimingManager API to access timestamp information. In each
variable, the FrameTimingManager records the time a specific event happens
during a frame.

The following table shows the values available through the API, in the order
that Unity executes them during a frame:

**Property** | **Description**  
---|---  
**frameStartTimestamp** | The CPU clock time when the frame begins.  
**firstSubmitTimestamp** | The CPU clock time when Unity submits the first job to the GPU during this frame.  
**cpuTimePresentCalled** | The CPU clock time when Unity calls the Present() function for the current frame.  
**cpuTimeFrameComplete** | The CPU clock time when the GPU finishes rendering the frame and interrupts the CPU.  
  
[](frame-timing-manager-enable.html)

Enable the FrameTimingManager

[](frame-timing-manager-record-timing-data.html)

Record frame timing data

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

