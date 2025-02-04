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

#  [ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html).GetSample

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

## Declaration

public
[Unity.Profiling.ProfilerRecorderSample](Unity.Profiling.ProfilerRecorderSample.html)
GetSample(int index);

### Description

Gets sample data.

Use to obtain sample data.

    
    
    using Unity.Profiling;
    using UnityEngine;  
      
    public class FrameTimeScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html) frameTimeRecorder;  
      
        void OnEnable()
        {
            frameTimeRecorder = [ProfilerRecorder.StartNew](Unity.Profiling.ProfilerRecorder.StartNew.html)([ProfilerCategory.Internal](Unity.Profiling.ProfilerCategory.Internal.html), "Main Thread", 30);
        }  
      
        void OnDisable()
        {
            frameTimeRecorder.Dispose();
        }  
      
        double CalculateAverageFromSampleValuesPerFrame([ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html) r)
        {
            int count = r.Count;
            double acc = 0;
            for (var i = 0; i < count; ++i)
            {
                acc += r.GetSample(i).Value;
            }
            return count > 0 ? acc / count : 0;
        }  
      
        void OnGUI()
        {
            [GUI.TextArea](GUI.TextArea.html)(new [Rect](Rect.html)(10, 30, 350, 20), $"Frame time: {CalculateAverageFromSampleValuesPerFrame(frameTimeRecorder) * 1e-6:0.00}ms");
        }
    }
    

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

