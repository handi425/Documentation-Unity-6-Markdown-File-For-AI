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

#  [ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html).LastValue

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

public long LastValue;

### Description

Gets the last value collected by the ProfilerRecorder.

Use to get the profiler counter value or marker timing capured at the end of
the last frame.  
  
The immediate value that
[CurrentValue](Unity.Profiling.ProfilerRecorder.CurrentValue.html) provides
might be not the final value of a counter when frame ends. For example,
rendering might happen after the logic finished computing the frame.
Therefore, it is impossible to get the final value of draw calls until the
frame is fully rendered. In such cases, you can use the LastValue property for
quick access to the final metric value in the last frame. The equivalent call
is `GetSample(Count - 1).Value`.  
  
**Note:** The property requires that the sample storage is non-zero. If the
capacity is 0, then this property returns 0.

    
    
    using Unity.Profiling;
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html) mainThreadTimeRecorder;  
      
        static double GetRecorderFrameAverage([ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html) recorder)
        {
            var samplesCount = recorder.Capacity;
            if (samplesCount == 0)
                return 0;  
      
            double r = 0;
            unsafe
            {
                var samples = stackalloc [ProfilerRecorderSample](Unity.Profiling.ProfilerRecorderSample.html)[samplesCount];
                recorder.CopyTo(samples, samplesCount);
                for (var i = 0; i < samplesCount; ++i)
                    r += samples[i].Value;
                r /= samplesCount;
            }  
      
            return r;
        }  
      
        void OnEnable()
        {
            mainThreadTimeRecorder = [ProfilerRecorder.StartNew](Unity.Profiling.ProfilerRecorder.StartNew.html)([ProfilerCategory.Internal](Unity.Profiling.ProfilerCategory.Internal.html), "Main Thread", 15);
        }  
      
        void OnDisable()
        {
            mainThreadTimeRecorder.Dispose();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [Debug.Log](Debug.Log.html)($"Frame [Time](Time.html): {GetRecorderFrameAverage(mainThreadTimeRecorder) * (1e-6f):F1} ms");
        }
    }
    

Use _LastValue_ to retrieve timings of a code tagged with
[ProfilerMarker.Auto](Unity.Profiling.ProfilerMarker.Auto.html).

    
    
    using UnityEngine;
    using Unity.Profiling;  
      
    public class Example
    {
        static readonly [ProfilerMarker](Unity.Profiling.ProfilerMarker.html) k_MyMarker = new [ProfilerMarker](Unity.Profiling.ProfilerMarker.html)([ProfilerCategory.Scripts](Unity.Profiling.ProfilerCategory.Scripts.html), "MyMarker");  
      
        public static void TimeSynchronousMethodWithMarkers()
        {
            using (var recorder = [ProfilerRecorder.StartNew](Unity.Profiling.ProfilerRecorder.StartNew.html)([ProfilerCategory.Scripts](Unity.Profiling.ProfilerCategory.Scripts.html), "MyMarker"))
            {
                using (k_MyMarker.Auto())
                {
                    // ...
                }  
      
                recorder.Stop();
                [Debug.Log](Debug.Log.html)("MyMarker total time, ns: " + recorder.LastValue);
            }
        }
    }
    

_LastValue_ only becomes readable and non-zero after a frame change or after
[Stop](Unity.Profiling.ProfilerRecorder.Stop.html) method call.

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

