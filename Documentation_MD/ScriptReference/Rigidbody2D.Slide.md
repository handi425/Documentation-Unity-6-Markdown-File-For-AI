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

#  [Rigidbody2D](Rigidbody2D.html).Slide

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

public [Rigidbody2D.SlideResults](Rigidbody2D.SlideResults.html)
Slide([Vector2](Vector2.html) velocity, float deltaTime,
[Rigidbody2D.SlideMovement](Rigidbody2D.SlideMovement.html) slideMovement);

### Parameters

velocity | The velocity to use when the [Rigidbody2D](Rigidbody2D.html) is sliding.  
---|---  
deltaTime | The time to integrate the `velocity` over.  
slideMovement | The configuration controlling of how the slide should be performed.  
  
### Returns

**SlideResults** The results of the slide movement.

### Description

Slide the [Rigidbody2D](Rigidbody2D.html) using the specified `velocity`
integrated over `deltaTime` using the configuration specified by
`slideMovement`.

The intent of this method is to provide fairly sophisticated movement with
minimal API. Movement includes sliding along surfaces within specific slope
angles, surface snapping, gravity and slippage on slopes within certain
angles. All contacts are handled automatically. This method can move a
[Rigidbody2D](Rigidbody2D.html) of any [body type](RigidbodyType2D.html) and
either immediately change the position, defer the position change until the
simulation step or simply return the calculated position.  
  
The following is a completely breakdown of the logic of this mechanism:  
  
The [Rigidbody2D](Rigidbody2D.html) can be moved using the specified
`velocity` integrated over the specified `deltaTime`. When this happens, any
contacts with other [Collider2D](Collider2D.html) will cause the appropriate
change in direction (velocity) to occur with no friction or bounce used. This
change in direction and subsequent continuation of movement using the
remaining velocity after the contact is known as a "slide". This is a single
slide iteration. A "slide" will only occur if the slope angle fo the surface
is less than that defined by
[Rigidbody2D.SlideMovement.surfaceSlideAngle](Rigidbody2D.SlideMovement-
surfaceSlideAngle.html). The maximum number of slide iterations allowed is
controlled by
[Rigidbody2D.SlideMovement.maxIterations](Rigidbody2D.SlideMovement-
maxIterations.html).  
  
When a slide iteration occurs, the velocity used to perform the move may cause
the [Rigidbody2D](Rigidbody2D.html) to move away from a
[Collider2D](Collider2D.html) surface. This would be seen if the slide moves
over a small ramp or is directed away from a surface when moving down a slope.
Often, this is not an intended behaviour so to counter this,
[Rigidbody2D.SlideMovement.surfaceAnchor](Rigidbody2D.SlideMovement-
surfaceAnchor.html) can be used to specify, during each iteration, the
direction and distance the slide iteration should look for a surface. Using
this, the slide can stay permanently "anchored" to a surface, even if the
velocity is moving it away. If this behaviour is not required then the
[Rigidbody2D.SlideMovement.surfaceAnchor](Rigidbody2D.SlideMovement-
surfaceAnchor.html) can be set to [Vector2.zero](Vector2-zero.html).  
  
The slide behavior will occur using multiple iterations until one of two
conditions are met:

  * The maximum number of iterations controlled by [Rigidbody2D.SlideMovement.maxIterations](Rigidbody2D.SlideMovement-maxIterations.html) has been reached.
  * The reamining distance has reached zero (as defined by the magnitude of the `velocity` (speed) over the `deltaTime` specified).

When the slide movement is complete as defined above, any gravity behaviour
requested will be handled if the provided
[Rigidbody2D.SlideMovement.gravity](Rigidbody2D.SlideMovement-gravity.html)
vector has a megnitude greater than zero. In this case, the
[Rigidbody2D](Rigidbody2D.html) is moved by the
[Rigidbody2D.SlideMovement.gravity](Rigidbody2D.SlideMovement-gravity.html)
scaled by the `deltaTime` specified. If the gravity movement causes a contact
to be found, the [Rigidbody2D](Rigidbody2D.html) is moved to that position.  
  
After this initial gravity movement, another slide iteration may occur in an
attempt to use all the remaining gravity movement. This extra gravity slide
iteration (slippage) will only occur if the following conditions are all met:

  * The contact is a surface whose slope angle is less than the slip angle defined by [Rigidbody2D.SlideMovement.gravitySlipAngle](Rigidbody2D.SlideMovement-gravitySlipAngle.html).
  * No initial `velocity` is specified i.e. no slip if movement is requested so slippage doesn't counter that movement.

In summary, calling the slide method using gravity will result in the
[Rigidbody2D](Rigidbody2D.html) moving with gravity but if no `velocity` is
specified, the [Rigidbody2D](Rigidbody2D.html) will slide/slip according to
the surface slope threshold specified by
Rigidbody2D.SlideMovement.surfaceSlipAngle.  
  
When the previously described behaviour is complete, a new
[Rigidbody2D](Rigidbody2D.html) position has been calculated however, the
[Rigidbody2D](Rigidbody2D.html) hasn't actually been moved at this stage. It
is here that the [Rigidbody2D](Rigidbody2D.html) can be instantly positioned
at the new position or the move can be deferred using
[Rigidbody2D.MovePosition](Rigidbody2D.MovePosition.html). This is controlled
with [Rigidbody2D.SlideMovement.useSimulationMove](Rigidbody2D.SlideMovement-
useSimulationMove.html). When this is enabled,
[Rigidbody2D.MovePosition](Rigidbody2D.MovePosition.html) is used whereas when
disabled, the [Rigidbody2D](Rigidbody2D.html) is instantly set at its new
position. It should be noted that both the [Rigidbody2D](Rigidbody2D.html) and
the [Transform](Transform.html) will be updated when
[Rigidbody2D.SlideMovement.useSimulationMove](Rigidbody2D.SlideMovement-
useSimulationMove.html) is disabled and that any
[Rigidbody2D](Rigidbody2D.html) interpolation continues to work as expected.  
  
The remaining configuration options allow more detailed control over the the
slide functionality. These are:

  * [Rigidbody2D.SlideMovement.startPosition](Rigidbody2D.SlideMovement-startPosition.html) can be used to override the start position of the slide, overriding the current [Rigidbody2D.position](Rigidbody2D-position.html).
  * [Rigidbody2D.SlideMovement.layerMask](Rigidbody2D.SlideMovement-layerMask.html) can be used to override which [Collider2D](Collider2D.html) are detected.
  * [Rigidbody2D.SlideMovement.useAttachedTriggers](Rigidbody2D.SlideMovement-useAttachedTriggers.html) can be used to select whether any [Collider2D](Collider2D.html) attached to this [Rigidbody2D](Rigidbody2D.html) (that are configured as a trigger) are used to detect contacts.
  * [Rigidbody2D.SlideMovement.selectedCollider](Rigidbody2D.SlideMovement-selectedCollider.html) can be used to select a specific [Collider2D](Collider2D.html) attached to this [Rigidbody2D](Rigidbody2D.html) to be used to detect contacts. If this is selected, the Rigidbody2D.SlideMovement.useTriggers is ignored.

**Note:** The slide method can be used on any
[RigidbodyType2D](RigidbodyType2D.html) but is mainly intended for use when
the [Rigidbody2D](Rigidbody2D.html) is Kinematic. No body type will interfere
with the slide method but using a Dynamic mode might produce unexpected
results because such a [Rigidbody2D](Rigidbody2D.html) can have their own
gravity, forces, collision-response etc. There is no performance penalty in
using any body type, Kinematic, Static or Dynamic and all are valid if
required. The Dynamic body type simply requires careful configuration so that
its inherent features don't cause conflicting and unexpected movement
behaviour.  
  
The following code uses a simple left/right keyboard input to set the relative
velocity left or right. The slide method will slide the
[Rigidbody2D](Rigidbody2D.html) using the configuration specified in the
[SlideMovement](Rigidbody2D.SlideMovement.html) and return the results of the
slide in [SlideResults](Rigidbody2D.SlideResults.html):

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Rigidbody2D.SlideMovement](Rigidbody2D.SlideMovement.html) [SlideMovement](Rigidbody2D.SlideMovement.html) = new [Rigidbody2D.SlideMovement](Rigidbody2D.SlideMovement.html)();
        public [Rigidbody2D.SlideResults](Rigidbody2D.SlideResults.html) [SlideResults](Rigidbody2D.SlideResults.html);  
      
        public float HorizontalSpeed = 2f;  
      
        private [Rigidbody2D](Rigidbody2D.html) m_Rigidbody;  
      
        void Start()
        {
            m_Rigidbody = GetComponent<[Rigidbody2D](Rigidbody2D.html)>();
       }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Calculate the horizontal velocity from keyboard input.
            var horizontalInput = ([Input.GetKey](Input.GetKey.html)([KeyCode.LeftArrow](KeyCode.LeftArrow.html)) ? -1 : 0f) + ([Input.GetKey](Input.GetKey.html)([KeyCode.RightArrow](KeyCode.RightArrow.html)) ? 1f : 0f);
            var velocity = new [Vector2](Vector2.html)(horizontalInput * HorizontalSpeed, 0f);  
      
            // Slide the rigidbody.
            [SlideResults](Rigidbody2D.SlideResults.html) = m_Rigidbody.Slide(velocity, [Time.deltaTime](Time-deltaTime.html), [SlideMovement](Rigidbody2D.SlideMovement.html));
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

