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

#  [Keyframe](Keyframe.html).outWeight

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

public float outWeight;

### Description

Sets the outgoing weight for this key. The outgoing weight affects the slope
of the curve from this key to the next key.

The weight is a value between 0 and 1. Set [weightedMode](Keyframe-
weightedMode.html) to [WeightedMode.Out](WeightedMode.Out.html) or
[WeightedMode.Both](WeightedMode.Both.html) to include weight when calculating
the slope of the outgoing curve.  
  
Additional resources: [inWeight](Keyframe-inWeight.html).

    
    
    using UnityEngine;  
      
    public class KeyFrameWeightExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [AnimationCurve](AnimationCurve.html)  animCurve = null;  
      
        void Start()
        {
            [Keyframe](Keyframe.html)[] ks = new [Keyframe](Keyframe.html)[3];  
      
            ks[0] = new [Keyframe](Keyframe.html)(0, 0);
            ks[0].weightedMode = [WeightedMode.Out](WeightedMode.Out.html);
            ks[0].outWeight = 0.5f;  
      
            ks[1] = new [Keyframe](Keyframe.html)(4, 0);
            ks[1].weightedMode = [WeightedMode.Out](WeightedMode.Out.html);
            ks[1].outWeight = 0f;    // Zero weight.  The segment will be linear if next keyframe [inWeight](Keyframe-inWeight.html) is also zero.  
      
            ks[2] = new [Keyframe](Keyframe.html)(6, 0);
            ks[2].weightedMode = [WeightedMode.Out](WeightedMode.Out.html);
            ks[2].outWeight = 1f / 3f;    // 1/3 is the default weight in [WeightedMode.None](WeightedMode.None.html) weightedMode.  
      
            animCurve = new [AnimationCurve](AnimationCurve.html)(ks);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if (animCurve != null)
                transform.position = new [Vector3](Vector3.html)([Time.time](Time-time.html), animCurve.Evaluate([Time.time](Time-time.html)), 0);
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

