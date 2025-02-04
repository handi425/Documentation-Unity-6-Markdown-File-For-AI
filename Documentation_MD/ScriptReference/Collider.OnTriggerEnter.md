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

#  [Collider](Collider.html).OnTriggerEnter(Collider)

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

### Parameters

other | The other [Collider](Collider.html) involved in this collision.  
---|---  
  
### Description

Called when a Collider with the [Collider.isTrigger](Collider-isTrigger.html)
property overlaps another Collider.

OnTriggerEnter is invoked when two GameObjects with a Collider component touch
or overlap, and one of the Collider components has the
[Collider.isTrigger](Collider-isTrigger.html) property enabled. A trigger
Collider doesn't register collisions with an incoming Rigidbody and doesn't
collide with any other GameObjects that have Colliders on them. The events are
invoked during simulation, which happens after all FixedUpdate methods are
called, or within the scope of [Physics.Simulate](Physics.Simulate.html), if
you're using manual physics simulation.  
  
Any Collider on a GameObject that has a Rigidbody component, or on a child of
a GameObject with a Rigidbody component can create OnTrigger events.  
  
To use the following code sample, create a primitive
[GameObject](GameObject.html), and attach a [Collider](Collider.html) and
[Rigidbody](Rigidbody.html) component to it. Enable Collider.isTrigger and
Rigidbody.isKinematic. This GameObject will travel forward, until it collides
with another GameObject. When a collision occurs, the direction immediately
reverses.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        private float speed = 2f;  
      
        //Moves this [GameObject](GameObject.html) 2 units a second in the forward direction
        void [Update](PlayerLoop.Update.html)()
        {
            transform.Translate([Vector3.forward](Vector3-forward.html) * [Time.deltaTime](Time-deltaTime.html) * speed);
        }  
      
        //Upon collision with another [GameObject](GameObject.html), this [GameObject](GameObject.html) will reverse direction
        private void OnTriggerEnter([Collider](Collider.html) other)
        {
            speed = speed * -1;
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

