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

#  [Transform](Transform.html).Find

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

[Switch to Manual](../Manual/class-Transform.html "Go to Transform Component
in the Manual")

## Declaration

public [Transform](Transform.html) Find(string n);

### Parameters

n | The search string, either the name of an immediate child or a hierarchy path for finding a descendent.  
---|---  
  
### Returns

**Transform** The found child transform. Null if child with matching name
isn't found.

### Description

Finds a child by name `n` and returns it.

If no child with name `n` can be found, null is returned. If `n` contains a
'/' character it will access the Transform in the hierarchy like a path name.  
  
**Note:** [Find](Transform.Find.html) does not work properly if you have '/'
in the name of a GameObject.  
**Note:** [Find](Transform.Find.html) does not perform a recursive descend
down a Transform hierarchy.  
**Note:** [Find](Transform.Find.html) can find transform of disabled
GameObject.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) player;
        public [Transform](Transform.html) gun;
        public [Transform](Transform.html) ammo;  
      
        //Invoked when a button is clicked.
        public void Example()
        {
            //Finds and assigns the child named "Gun".
            gun = player.transform.Find("Gun");  
      
            //If the child was found.
            if (gun != null)
            {
                //Find the child named "ammo" of the gameobject "magazine" (magazine is a child of "gun").
                ammo = gun.transform.Find("magazine/ammo");
            }
            else [Debug.Log](Debug.Log.html)("No child with the name 'Gun' attached to the player");
        }
    }
    

As described [Find](Transform.Find.html) does not descend the
[Transform](Transform.html) hierarchy. [Find](Transform.Find.html) will only
search the given list of children looking for a named
[Transform](Transform.html). The following example shows the result of
[Find](Transform.Find.html) searching for GameObjects. The name of each
GameObject is used in the [Find](Transform.Find.html). This is why two
GameObjects in the same level of the hierarchy are found and reported.  
  
![](../StaticFiles/ScriptRefImages/TransformFind.png)  
_A GameObject with three children. Find() does not find the third child._

    
    
    // ExampleClass has a [GameObject](GameObject.html) with three spheres attached.
    // Two of these are children of the [GameObject](GameObject.html).  The third
    // transform, sphere3, is a child of sphere2.  Find() does
    // not find this child.  
      
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Transform](Transform.html) result;  
      
            for (int i = 1; i < 4; i++)
            {
                string sph;  
      
                sph = "sphere" + i.ToString();
                result = gameObject.transform.Find(sph);  
      
                if (result)
                {
                    [Debug.Log](Debug.Log.html)("Found: " + sph);
                }
                else
                {
                    //Find() does not find sphere3
                    [Debug.Log](Debug.Log.html)("Did not find: " + sph);  
      
                    //But we can access it with '/' character or by using GetChild()
                    [Transform](Transform.html) newresult;
                    newresult = gameObject.transform.Find("sphere2/sphere3");  
      
                    if (newresult)
                    {
                        [Debug.Log](Debug.Log.html)("But now found:" + sph);
                    }
                }
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

