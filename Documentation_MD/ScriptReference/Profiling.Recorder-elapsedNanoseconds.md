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

#  [Recorder](Profiling.Recorder.html).elapsedNanoseconds

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

public long elapsedNanoseconds;

### Description

Accumulated time of Begin/End pairs for the previous frame in nanoseconds.
(Read Only)

Long-lasting operations (for example, on a preloading thread) might not end
within a single frame. In this case, **elapsedNanoseconds** is calculated
until the end of the frame, so you can always see activity for these
operations.

    
    
    using UnityEngine;
    using UnityEngine.Profiling;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        [Recorder](Profiling.Recorder.html) behaviourUpdateRecorder;
        void Start()
        {
            behaviourUpdateRecorder = [Recorder.Get](Profiling.Recorder.Get.html)("BehaviourUpdate");
            behaviourUpdateRecorder.enabled = true;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if (behaviourUpdateRecorder.isValid)
                [Debug.Log](Debug.Log.html)("BehaviourUpdate time: " + behaviourUpdateRecorder.elapsedNanoseconds);
        }
    }
    

Use _elapsedNanoseconds_ to retrieve timings of a code tagged with
[ProfilerMarker.Auto](Unity.Profiling.ProfilerMarker.Auto.html).

    
    
    using UnityEngine;
    using UnityEngine.Profiling;  
      
    public class Example
    {
        public static void TimeSynchronousMethodWithMarkers()
        {
            var recorder = [Recorder.Get](Profiling.Recorder.Get.html)("MyMarker");
            recorder.enabled = true; // Start measurements  
      
            // Call method which uses MyMarker
            // MyMethod();  
      
            recorder.enabled = false; // Stops measurements and makes data available immediately
            [Debug.Log](Debug.Log.html)("MyMarker total time, ns: " + recorder.elapsedNanoseconds);
        }
    }
    

In synchronous measurements that don't involve a frame change,
_elapsedNanoseconds_ only becomes a non-zero value after the Recorder is
disabled.

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

