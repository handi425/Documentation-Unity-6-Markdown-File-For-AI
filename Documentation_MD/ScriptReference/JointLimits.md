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

# JointLimits

struct in UnityEngine

/

Implemented in:[UnityEngine.PhysicsModule](UnityEngine.PhysicsModule.html)

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

JointLimits is used by the [HingeJoint](HingeJoint.html) to limit the joints
angle.

Additional resources: [HingeJoint](HingeJoint.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Set the hinge limits for a door.
            [HingeJoint](HingeJoint.html) hinge = GetComponent<[HingeJoint](HingeJoint.html)>();  
      
            [JointLimits](JointLimits.html) limits = hinge.limits;
            limits.min = 0;
            limits.max = 90;
            limits.bounciness = 0;
            limits.bounceMinVelocity = 0;
            hinge.limits = limits;
        }
    }
    

### Properties

[bounceMinVelocity](JointLimits-bounceMinVelocity.html)| The minimum impact
velocity which will cause the joint to bounce.  
---|---  
[bounciness](JointLimits-bounciness.html)| Determines the size of the bounce
when the joint hits it's limit. Also known as restitution.  
[contactDistance](JointLimits-contactDistance.html)| Distance inside the limit
value at which the limit will be considered to be active by the solver.  
[max](JointLimits-max.html)| The upper angular limit (in degrees) of the
joint.  
[min](JointLimits-min.html)| The lower angular limit (in degrees) of the
joint.  
  
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

