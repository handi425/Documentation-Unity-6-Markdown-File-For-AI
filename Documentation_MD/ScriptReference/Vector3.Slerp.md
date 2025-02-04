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

#  [Vector3](Vector3.html).Slerp

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

public static [Vector3](Vector3.html) Slerp([Vector3](Vector3.html) a,
[Vector3](Vector3.html) b, float t);

### Description

Spherically interpolates between two vectors.

Interpolates between `a` and `b` by amount `t`. The difference between this
and linear interpolation (aka, "lerp") is that the vectors are treated as
directions rather than points in space. The direction of the returned vector
is interpolated by the angle and its [magnitude](Vector3-magnitude.html) is
interpolated between the magnitudes of `from` and `to`.  
  
The parameter `t` is clamped to the range [0, 1].

    
    
    // Animates the position in an arc between sunrise and sunset.  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html) sunrise;
        public [Transform](Transform.html) sunset;  
      
        // [Time](Time.html) to move from sunrise to sunset position, in seconds.
        public float journeyTime = 1.0f;  
      
        // The time at which the animation started.
        private float startTime;  
      
        void Start()
        {
            // Note the time at the start of the animation.
            startTime = [Time.time](Time-time.html);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // The center of the arc
            [Vector3](Vector3.html) center = (sunrise.position + sunset.position) * 0.5F;  
      
            // move the center a bit downwards to make the arc vertical
            center -= new [Vector3](Vector3.html)(0, 1, 0);  
      
            // Interpolate over the arc relative to center
            [Vector3](Vector3.html) riseRelCenter = sunrise.position - center;
            [Vector3](Vector3.html) setRelCenter = sunset.position - center;  
      
            // The fraction of the animation that has happened so far is
            // equal to the elapsed time divided by the desired time for
            // the total journey.
            float fracComplete = ([Time.time](Time-time.html) - startTime) / journeyTime;  
      
            transform.position = [Vector3.Slerp](Vector3.Slerp.html)(riseRelCenter, setRelCenter, fracComplete);
            transform.position += center;
        }
    }
    

Additional resources: [Lerp](Vector3.Lerp.html),
[SlerpUnclamped](Vector3.SlerpUnclamped.html).

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

