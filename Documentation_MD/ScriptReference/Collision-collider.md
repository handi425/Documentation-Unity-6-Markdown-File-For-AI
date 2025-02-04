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

#  [Collision](Collision.html).collider

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

public [Collider](Collider.html) collider;

### Description

The [Collider](Collider.html) we hit (Read Only).

Fetch the Collider of the GameObject your GameObject hits. To find all
colliders that were hit in detail you have to iterate the contact points
([contacts](Collision-contacts.html) property).

    
    
    //In this example, the name of the [GameObject](GameObject.html) that collides with your [GameObject](GameObject.html) is output to the console. Then this checks the name of the [Collider](Collider.html) and if it matches with the one you specify, it outputs another message.  
      
    //Create a [GameObject](GameObject.html) and make sure it has a [Collider](Collider.html) component. Attach this script to it.
    //Create a second [GameObject](GameObject.html) with a [Collider](Collider.html) and place it on top of the other [GameObject](GameObject.html) to output that there was a collision. You can add movement to the [GameObject](GameObject.html) to test more.  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        //If your [GameObject](GameObject.html) starts to collide with another [GameObject](GameObject.html) with a [Collider](Collider.html)
        void OnCollisionEnter([Collision](Collision.html) collision)
        {
            //Output the [Collider](Collider.html)'s [GameObject](GameObject.html)'s name
            [Debug.Log](Debug.Log.html)(collision.collider.name);
        }  
      
        //If your [GameObject](GameObject.html) keeps colliding with another [GameObject](GameObject.html) with a [Collider](Collider.html), do something
        void OnCollisionStay([Collision](Collision.html) collision)
        {
            //Check to see if the [Collider](Collider.html)'s name is "Chest"
            if (collision.collider.name == "Chest")
            {
                //Output the message
                [Debug.Log](Debug.Log.html)("Chest is here!");
            }
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

