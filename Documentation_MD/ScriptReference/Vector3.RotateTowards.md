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

#  [Vector3](Vector3.html).RotateTowards

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

public static [Vector3](Vector3.html) RotateTowards([Vector3](Vector3.html)
current, [Vector3](Vector3.html) target, float maxRadiansDelta, float
maxMagnitudeDelta);

### Parameters

current | The vector being managed.  
---|---  
target | The vector.  
maxRadiansDelta | The maximum angle in radians allowed for this rotation.  
maxMagnitudeDelta | The maximum allowed change in vector magnitude for this rotation.  
  
### Returns

**Vector3** The location that RotateTowards generates.

### Description

Rotates a vector `current` towards `target`.

This function is similar to [MoveTowards](Vector3.MoveTowards.html) except
that the vector is treated as a direction rather than a position. The
`current` vector will be rotated round toward the `target` direction by an
angle of `maxRadiansDelta`, although it will land exactly on the target rather
than overshoot. If the magnitudes of `current` and `target` are different,
then the magnitude of the result will be linearly interpolated during the
rotation. If a negative value is used for `maxRadiansDelta`, the vector will
rotate away from `target/` until it is pointing in exactly the opposite
direction, then stops.  
  
  
Additional resources:
[Quaternion.RotateTowards](Quaternion.RotateTowards.html).

    
    
    using UnityEngine;  
      
    // To use this script, attach it to the [GameObject](GameObject.html) that you would like to rotate towards another game object.
    // After attaching it, go to the inspector and drag the [GameObject](GameObject.html) you would like to rotate towards into the target field.
    // Move the target around in the scene view to see the [GameObject](GameObject.html) continuously rotate towards it.
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // The target marker.
        public [Transform](Transform.html) target;  
      
        // Angular speed in radians per sec.
        public float speed = 1.0f;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Determine which direction to rotate towards
            [Vector3](Vector3.html) targetDirection = target.position - transform.position;  
      
            // The step size is equal to speed times frame time.
            float singleStep = speed * [Time.deltaTime](Time-deltaTime.html);  
      
            // [Rotate](UIElements.Rotate.html) the forward vector towards the target direction by one step
            [Vector3](Vector3.html) newDirection = [Vector3.RotateTowards](Vector3.RotateTowards.html)(transform.forward, targetDirection, singleStep, 0.0f);  
      
            // Draw a ray pointing at our target in
            [Debug.DrawRay](Debug.DrawRay.html)(transform.position, newDirection, [Color.red](Color-red.html));  
      
            // Calculate a rotation a step closer to the target and applies rotation to this object
            transform.rotation = [Quaternion.LookRotation](Quaternion.LookRotation.html)(newDirection);
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

