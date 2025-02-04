[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/frame-timing-manager-record-timing-data.html)
  * [中文](/cn/current/Manual/frame-timing-manager-record-timing-data.html)
  * [日本語](/ja/current/Manual/frame-timing-manager-record-timing-data.html)
  * [한국어](/kr/current/Manual/frame-timing-manager-record-timing-data.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/frame-timing-manager-record-timing-data.html)
  * [中文](/cn/current/Manual/frame-timing-manager-record-timing-data.html)
  * [日本語](/ja/current/Manual/frame-timing-manager-record-timing-data.html)
  * [한국어](/kr/current/Manual/frame-timing-manager-record-timing-data.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Profile rendering](profile-rendering.html)
  * [Frame Timing Manager](frame-timing-manager-landing.html)
  * Record frame timing data

[](frame-timing-manager-get-timing-data.html)

Get frame timing data

[](frame-timing-manager-troubleshoot.html)

Troubleshooting the Frame Time Manager

# Record frame timing data

You can read FrameTimingManager values using the ProfilerRecorder API instead
of the FrameTimingManager C# API. The benefit of this is that when you use the
ProfilerRecorder API, the FrameTimingManager only records values when you
attach a recorder to a specific counter. This behavior enables you to control
which counters collect data and so, reduce the impact that the
FrameTimingManager has on performance.

The following example shows how to track only the CPU Main Thread Frame Time
variable with the ProfilerRecordAPI:

    
    
    using Unity.Profiling;
    
    using UnityEngine;
    
    public class ExampleScript : MonoBehaviour
    
    {
    
        string statsText;
    
        ProfilerRecorder mainThreadTimeRecorder;
    
        void OnEnable()
    
        {
            mainThreadTimeRecorder = ProfilerRecorder.StartNew(ProfilerCategory.Internal, "CPU Main Thread Frame Time");
        }
    
        void OnDisable()
    
        {
            mainThreadTimeRecorder.Dispose();
        }
    
        void Update()
    
        {
    
            var frameTime = mainThreadTimeRecorder.LastValue;
    
            // Your code logic here
    
        }
    }
    
    

[](frame-timing-manager-get-timing-data.html)

Get frame timing data

[](frame-timing-manager-troubleshoot.html)

Troubleshooting the Frame Time Manager

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

