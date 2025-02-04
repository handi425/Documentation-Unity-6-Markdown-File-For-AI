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

# SlideMovement

struct in UnityEngine

/

Implemented in:[UnityEngine.Physics2DModule](UnityEngine.Physics2DModule.html)

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

The configuration that controls how a
[Rigidbody2D.Slide](Rigidbody2D.Slide.html) method behaves.

**NOTE:** This struct can be used in the Unity Inspector for configuration
purposes.  
  
Additional resources: [Rigidbody2D.Slide](Rigidbody2D.Slide.html) and
[SlideResults](Rigidbody2D.SlideResults.html).

### Properties

[gravity](Rigidbody2D.SlideMovement-gravity.html)| The gravity to be applied
to the slide position.  
---|---  
[gravitySlipAngle](Rigidbody2D.SlideMovement-gravitySlipAngle.html)| When the
gravity movement causes a contact with a Collider2D, slippage maybe occur if
the surface angle is greater than this angle.  
[layerMask](Rigidbody2D.SlideMovement-layerMask.html)| A LayerMask that will
be used when determining what Collider2D should be detected.  
[maxIterations](Rigidbody2D.SlideMovement-maxIterations.html)| Controls the
maximum number of iterations to perform when determining how a Rigidbody2D
will slide.  
[selectedCollider](Rigidbody2D.SlideMovement-selectedCollider.html)| The
specific Collider2D attached to this Rigidbody2D to be used to detect
contacts.  
[startPosition](Rigidbody2D.SlideMovement-startPosition.html)| The start
position to slide the Rigidbody2D from.  
[surfaceAnchor](Rigidbody2D.SlideMovement-surfaceAnchor.html)| The direction
and distance to use when detecting if a surface is nearby during a slide
iteration.  
[surfaceSlideAngle](Rigidbody2D.SlideMovement-surfaceSlideAngle.html)| When
the velocity movement causes a contact with a Collider2D, a slide maybe occur
if the surface angle is less than this angle.  
[surfaceUp](Rigidbody2D.SlideMovement-surfaceUp.html)| A reference direction
used to calculate contact angles.  
[useAttachedTriggers](Rigidbody2D.SlideMovement-useAttachedTriggers.html)| Can
be used to select whether any Collider2D attached to this Rigidbody2D (that
are configured as a trigger) are used to detect contacts.  
[useLayerMask](Rigidbody2D.SlideMovement-useLayerMask.html)| Whether the
specified Rigidbody2D.SlideMovement.layerMask should be used or not when
determining what Collider2D should be detected.  
[useNoMove](Rigidbody2D.SlideMovement-useNoMove.html)| Controls if any
Rigidbody2D movement will happen or not.  
[useSimulationMove](Rigidbody2D.SlideMovement-useSimulationMove.html)|
Controls whether the Rigidbody2D is instantly moved to the calculated position
or is moved with Rigidbody2D.MovePosition.  
[useStartPosition](Rigidbody2D.SlideMovement-useStartPosition.html)| Whether
the specified Rigidbody2D.SlideMovement.startPosition should be used or not.  
  
### Public Methods

[SetLayerMask](Rigidbody2D.SlideMovement.SetLayerMask.html)| A helper method
that simultaneously sets both the Rigidbody2D.SlideMovement.layerMask to the
specified mask but also sets Rigidbody2D.SlideMovement.useLayerMask to true.  
---|---  
[SetStartPosition](Rigidbody2D.SlideMovement.SetStartPosition.html)| A helper
method that simultaneously sets both the
Rigidbody2D.SlideMovement.startPosition to the specified /position but also
sets Rigidbody2D.SlideMovement.useStartPosition to true.  
  
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

