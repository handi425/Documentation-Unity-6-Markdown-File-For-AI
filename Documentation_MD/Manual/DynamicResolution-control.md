[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/DynamicResolution-control.html)
  * [中文](/cn/current/Manual/DynamicResolution-control.html)
  * [日本語](/ja/current/Manual/DynamicResolution-control.html)
  * [한국어](/kr/current/Manual/DynamicResolution-control.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/DynamicResolution-control.html)
  * [中文](/cn/current/Manual/DynamicResolution-control.html)
  * [日本語](/ja/current/Manual/DynamicResolution-control.html)
  * [한국어](/kr/current/Manual/DynamicResolution-control.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [Changing resolution scale](resolution-scale.html)
  * [Dynamic Resolution](DynamicResolution-landing.html)
  * Control scaling with Dynamic Resolution

[](DynamicResolution-introduction.html)

Introduction to Dynamic Resolution

[](DynamicResolution-control-when-occurs.html)

Control when Dynamic Scaling happens

# Control scaling with Dynamic Resolution

You can control the scale through the
[ScalableBufferManager](../ScriptReference/ScalableBufferManager.html). The
[ScalableBufferManager](../ScriptReference/ScalableBufferManager.html) gives
you control of the dynamic width and height scale for all render targets you
have marked for the **dynamic resolution** A Camera setting that allows you to
dynamically scale individual render targets to reduce workload on the GPU.
[More info](DynamicResolution-landing.html)  
See in [Glossary](Glossary.html#dynamicresolution) system to scale.

As an example, assume your application is running at a desirable frame rate,
but under some circumstances the GPU performance decreases, due to a
combination of increased particles, post-effects and screen complexity. The
Unity [FrameTimingManager](../ScriptReference/FrameTimingManager.html) allows
you to detect when the CPU or GPU performance start to decrease. So you can
use the `FrameTimingManager` to calculate a new desired width and height scale
to keep the frame rate within your desired range, and bring the scale down to
that value to keep performance stable (either instantly or gradually over a
set amount of frames). When the screen complexity reduces and the GPU is
performing consistently, you may then raise the width and height scale back to
a value that you’ve calculated the GPU can handle.

## Example

This example script demonstrates basic use of the API. Add it to a Camera in
your Scene, and check **Allow Dynamic Resolution** in the Camera settings. You
also need to open the **Player** settings (menu: **Edit > Project Settings**,
then select the **Player** category) and check the **Enable Frame Timing
Stats** checkbox. For more information about the functionality behind the
**Enable Frame Timing Stats** property, see [FrameTimingManager](frame-timing-
manager.html).

Clicking the mouse, or tapping the screen with one finger, lowers the height
and width resolution by the amount in the `scaleWidthIncrement` and
`scaleHeightIncrement` variables respectively. Tapping with two fingers raises
the resolutions by the same increment.

    
    
    using System;
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.UI;
    
    public class DynamicResolutionTest : MonoBehaviour
    {
        public Text screenText;
    
        FrameTiming[] frameTimings = new FrameTiming[3];
    
        public float maxResolutionWidthScale = 1.0f;
        public float maxResolutionHeightScale = 1.0f;
        public float minResolutionWidthScale = 0.5f;
        public float minResolutionHeightScale = 0.5f;
        public float scaleWidthIncrement = 0.1f;
        public float scaleHeightIncrement = 0.1f;
    
        float m_widthScale = 1.0f;
        float m_heightScale = 1.0f;
    
        // Variables for dynamic resolution algorithm that persist across frames
        uint m_frameCount = 0;
    
        const uint kNumFrameTimings = 2;
    
        double m_gpuFrameTime;
        double m_cpuFrameTime;
    
        // Use this for initialization
        void Start()
        {
            int rezWidth = (int)Mathf.Ceil(ScalableBufferManager.widthScaleFactor * Screen.currentResolution.width);
            int rezHeight = (int)Mathf.Ceil(ScalableBufferManager.heightScaleFactor * Screen.currentResolution.height);
            screenText.text = string.Format("Scale: {0:F3}x{1:F3}\nResolution: {2}x{3}\n",
                m_widthScale,
                m_heightScale,
                rezWidth,
                rezHeight);
        }
    
        // Update is called once per frame
        void Update()
        {
            float oldWidthScale = m_widthScale;
            float oldHeightScale = m_heightScale;
    
            // One finger lowers the resolution
            if (Input.GetButtonDown("Fire1"))
            {
                m_heightScale = Mathf.Max(minResolutionHeightScale, m_heightScale - scaleHeightIncrement);
                m_widthScale = Mathf.Max(minResolutionWidthScale, m_widthScale - scaleWidthIncrement);
            }
    
            // Two fingers raises the resolution
            if (Input.GetButtonDown("Fire2"))
            {
                m_heightScale = Mathf.Min(maxResolutionHeightScale, m_heightScale + scaleHeightIncrement);
                m_widthScale = Mathf.Min(maxResolutionWidthScale, m_widthScale + scaleWidthIncrement);
            }
    
            if (m_widthScale != oldWidthScale || m_heightScale != oldHeightScale)
            {
                ScalableBufferManager.ResizeBuffers(m_widthScale, m_heightScale);
            }
            DetermineResolution();
            int rezWidth = (int)Mathf.Ceil(ScalableBufferManager.widthScaleFactor * Screen.currentResolution.width);
            int rezHeight = (int)Mathf.Ceil(ScalableBufferManager.heightScaleFactor * Screen.currentResolution.height);
            screenText.text = string.Format("Scale: {0:F3}x{1:F3}\nResolution: {2}x{3}\nScaleFactor: {4:F3}x{5:F3}\nGPU: {6:F3} CPU: {7:F3}",
                m_widthScale,
                m_heightScale,
                rezWidth,
                rezHeight,
                ScalableBufferManager.widthScaleFactor,
                ScalableBufferManager.heightScaleFactor,
                m_gpuFrameTime,
                m_cpuFrameTime);
        }
    
        // Estimate the next frame time and update the resolution scale if necessary.
        private void DetermineResolution()
        {
            ++m_frameCount;
            if (m_frameCount <= kNumFrameTimings)
            {
                return;
            }
            FrameTimingManager.CaptureFrameTimings();
            FrameTimingManager.GetLatestTimings(kNumFrameTimings, frameTimings);
            if (frameTimings.Length < kNumFrameTimings)
            {
                Debug.LogFormat("Skipping frame {0}, didn't get enough frame timings.",
                    m_frameCount);
    
                return;
            }
    
            m_gpuFrameTime = (double)frameTimings[0].gpuFrameTime;
            m_cpuFrameTime = (double)frameTimings[0].cpuFrameTime;
        }
    }
    

[](DynamicResolution-introduction.html)

Introduction to Dynamic Resolution

[](DynamicResolution-control-when-occurs.html)

Control when Dynamic Scaling happens

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

