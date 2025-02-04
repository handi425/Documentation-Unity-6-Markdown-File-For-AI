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

#  [Collider](Collider.html).OnTriggerExit(Collider)

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

other | The other Collider involved in this collision.  
---|---  
  
### Description

OnTriggerExit is called when the [Collider](Collider.html) `other` has stopped
touching the trigger.

This message is sent to the trigger and the Collider that touches the trigger.  
  
**Notes:** Trigger events are only sent if one of the Colliders also has a
Rigidbody attached. Trigger events will be sent to disabled MonoBehaviours, to
allow enabling Behaviours in response to collisions.
[OnTriggerExit](Collider.OnTriggerExit.html) occurs on the FixedUpdate after
the Colliders have stopped touching. The Colliders involved are not guaranteed
to be at the point of initial separation. Deactivating or destroying a
Collider while it is inside a trigger volume will not register an on exit
event.  
  
Additional resources: [Collider.OnTriggerEnter](Collider.OnTriggerEnter.html)
which contains a useful example.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnTriggerExit([Collider](Collider.html) other)
        {
            // Destroy everything that leaves the trigger
            Destroy(other.gameObject);
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

