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

# ProfilerRecorder

struct in Unity.Profiling

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

Records the Profiler metric data that a Profiler marker or counter produces.

Use ProfilerRecorder to access performance metrics that the Profiler exposes.
You can use it to read Profiler counter data such as memory or render
statistics, and Profiler marker timing data in a uniform way.  
  
You can use this API in Editor and Player builds, including Release Players.
Use
[ProfilerRecorderHandle.GetAvailable](Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderHandle.GetAvailable.html)
to get the full list of supported metrics. For a list of built-in Profiler
markers available, see the User Manual documentation on [Common Profiler
markers](../Manual/profiler-markers.html).  
  
The following example demonstrates how you can use ProfilerRecorder to get
memory and timing statistics.

    
    
    using System.Collections.Generic;
    using System.Text;
    using Unity.Profiling;
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        string statsText;
        [ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html) systemMemoryRecorder;
        [ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html) gcMemoryRecorder;
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
            systemMemoryRecorder = [ProfilerRecorder.StartNew](Unity.Profiling.ProfilerRecorder.StartNew.html)([ProfilerCategory.Memory](Unity.Profiling.ProfilerCategory.Memory.html), "[System](Rendering.VirtualTexturing.System.html) Used Memory");
            gcMemoryRecorder = [ProfilerRecorder.StartNew](Unity.Profiling.ProfilerRecorder.StartNew.html)([ProfilerCategory.Memory](Unity.Profiling.ProfilerCategory.Memory.html), "GC Reserved Memory");
            mainThreadTimeRecorder = [ProfilerRecorder.StartNew](Unity.Profiling.ProfilerRecorder.StartNew.html)([ProfilerCategory.Internal](Unity.Profiling.ProfilerCategory.Internal.html), "Main Thread", 15);
        }  
      
        void OnDisable()
        {
            systemMemoryRecorder.Dispose();
            gcMemoryRecorder.Dispose();
            mainThreadTimeRecorder.Dispose();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var sb = new StringBuilder(500);
            sb.AppendLine($"Frame [Time](Time.html): {GetRecorderFrameAverage(mainThreadTimeRecorder) * (1e-6f):F1} ms");
            sb.AppendLine($"GC Memory: {gcMemoryRecorder.LastValue / (1024 * 1024)} MB");
            sb.AppendLine($"[System](Rendering.VirtualTexturing.System.html) Memory: {systemMemoryRecorder.LastValue / (1024 * 1024)} MB");
            statsText = sb.ToString();
        }  
      
        void OnGUI()
        {
            [GUI.TextArea](GUI.TextArea.html)(new [Rect](Rect.html)(10, 30, 250, 50), statsText);
        }
    }
    

**Note:**  
ProfilerRecorder allocates unmanaged resources and implements IDisposable
interface. Use [Dispose](Unity.Profiling.ProfilerRecorder.Dispose.html) to
free resources when you no longer need to record statistics.  
  
ProfilerRecorder gives you access to Unity metrics in two modes: immediate
access to a value of a counter, and the counter value when the frame ends.
Additional resources:
[CurrentValue](Unity.Profiling.ProfilerRecorder.CurrentValue.html),
[LastValue](Unity.Profiling.ProfilerRecorder.LastValue.html),
[GetSample](Unity.Profiling.ProfilerRecorder.GetSample.html),
[ProfilerRecorderHandle.GetAvailable](Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderHandle.GetAvailable.html).

### Properties

[Capacity](Unity.Profiling.ProfilerRecorder.Capacity.html)| Maximum amount of
samples ProfilerRecorder can capture.  
---|---  
[Count](Unity.Profiling.ProfilerRecorder.Count.html)| Collected samples count.  
[CurrentValue](Unity.Profiling.ProfilerRecorder.CurrentValue.html)| Gets
current value of the Profiler metric.  
[CurrentValueAsDouble](Unity.Profiling.ProfilerRecorder.CurrentValueAsDouble.html)|
Gets current value of the Profiler metric as double value.  
[DataType](Unity.Profiling.ProfilerRecorder.DataType.html)| Value data type of
the Profiler metric.  
[IsRunning](Unity.Profiling.ProfilerRecorder.IsRunning.html)| Indicates if
ProfilerRecorder is attached to the Profiler metric.  
[LastValue](Unity.Profiling.ProfilerRecorder.LastValue.html)| Gets the last
value collected by the ProfilerRecorder.  
[LastValueAsDouble](Unity.Profiling.ProfilerRecorder.LastValueAsDouble.html)|
Gets the last value collected by the ProfilerRecorder as double.  
[UnitType](Unity.Profiling.ProfilerRecorder.UnitType.html)| Unit type.  
[Valid](Unity.Profiling.ProfilerRecorder.Valid.html)| Indicates whether
ProfilerRecorder is associated with a valid Profiler marker or counter.  
[WrappedAround](Unity.Profiling.ProfilerRecorder.WrappedAround.html)|
Indicates if ProfilerRecorder capacity has been exceeded.  
  
### Constructors

[ProfilerRecorder](Unity.Profiling.ProfilerRecorder-ctor.html)| Constructs
ProfilerRecorder instance with a Profiler metric name and category.  
---|---  
  
### Public Methods

[CopyTo](Unity.Profiling.ProfilerRecorder.CopyTo.html)| Copies collected
samples to the destination array.  
---|---  
[Dispose](Unity.Profiling.ProfilerRecorder.Dispose.html)| Releases unmanaged
instance of the ProfilerRecorder.  
[GetSample](Unity.Profiling.ProfilerRecorder.GetSample.html)| Gets sample
data.  
[Reset](Unity.Profiling.ProfilerRecorder.Reset.html)| Stops data collection
and clears collected samples.  
[Start](Unity.Profiling.ProfilerRecorder.Start.html)| Start data collection.  
[Stop](Unity.Profiling.ProfilerRecorder.Stop.html)| Stops data collection.  
[ToArray](Unity.Profiling.ProfilerRecorder.ToArray.html)| Use to convert
collected samples to an array.  
  
### Static Methods

[StartNew](Unity.Profiling.ProfilerRecorder.StartNew.html)| Initialize a new
instance of ProfilerRecorder and start data collection.  
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

