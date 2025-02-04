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

#  [Collision](Collision.html).gameObject

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

public [GameObject](GameObject.html) gameObject;

### Description

The [GameObject](GameObject.html) whose collider you are colliding with. (Read
Only).

This is the GameObject that is colliding with your GameObject. Access this to
check properties of the colliding GameObject, for example, the GameObject’s
name and tag.

    
    
    using UnityEngine;  
      
    public class CollisionGameObjectExample : [MonoBehaviour](MonoBehaviour.html)
    {
        //Detect collisions between the GameObjects with Colliders attached
        void OnCollisionEnter([Collision](Collision.html) collision)
        {
            //Check for a match with the specified name on any [GameObject](GameObject.html) that collides with your [GameObject](GameObject.html)
            if (collision.gameObject.name == "MyGameObjectName")
            {
                //If the [GameObject](GameObject.html)'s name matches the one you suggest, output this message in the console
                [Debug.Log](Debug.Log.html)("Do something here");
            }  
      
            //Check for a match with the specific tag on any [GameObject](GameObject.html) that collides with your [GameObject](GameObject.html)
            if (collision.gameObject.tag == "MyGameObjectTag")
            {
                //If the [GameObject](GameObject.html) has the same tag as specified, output this message in the console
                [Debug.Log](Debug.Log.html)("Do something else here");
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

