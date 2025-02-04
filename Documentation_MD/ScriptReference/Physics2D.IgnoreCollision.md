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

#  [Physics2D](Physics2D.html).IgnoreCollision

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

public static void IgnoreCollision([Collider2D](Collider2D.html) collider1,
[Collider2D](Collider2D.html) collider2, bool ignore = true);

### Parameters

collider1 | The first Collider to compare to `collider2`.  
---|---  
collider2 | The second Collider to compare to `collider1`.  
ignore | Whether collisions/triggers between `collider1` and `collider2` should be ignored or not.  
  
### Description

Makes the collision detection system ignore all collisions/triggers between
`collider1` and `collider2`.

Ignoring collisions refers to any type of interaction between the selected
Colliders i.e. no collision or trigger interaction will occur. Collision
layers are first checked to see the two layers can interact and if not then no
interactions take place. Following that, ignoring specific Colliders
interactions will occur.  
  
IgnoreCollision has a few limitations: 1) It is not persistent. This means
that the ignore collision state will not be stored in the editor when saving a
Scene. 2) You can only apply the ignore collision to Colliders in active game
objects. When deactivating the Collider the IgnoreCollision state will be lost
and you have to call Physics2D.IgnoreCollision again. Additional resources:
[Physics2D.GetIgnoreCollision](Physics2D.GetIgnoreCollision.html),
[Physics2D.IgnoreLayerCollision](Physics2D.IgnoreLayerCollision.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Instantiate a bullet and make it ignore collisions with this object.  
      
        [Transform](Transform.html) bulletPrefab;  
      
        void Start()
        {
            var bullet = Instantiate(bulletPrefab) as [Transform](Transform.html);
            [Physics2D.IgnoreCollision](Physics2D.IgnoreCollision.html)(bullet.GetComponent<[Collider2D](Collider2D.html)>(), GetComponent<[Collider2D](Collider2D.html)>());
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

