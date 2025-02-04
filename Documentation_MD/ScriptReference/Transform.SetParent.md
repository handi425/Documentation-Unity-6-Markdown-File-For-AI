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

#  [Transform](Transform.html).SetParent

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

public void SetParent([Transform](Transform.html) p);

## Declaration

public void SetParent([Transform](Transform.html) parent, bool
worldPositionStays);

### Parameters

parent | The parent Transform to use.  
---|---  
worldPositionStays | If true, the parent-relative position, scale and rotation are modified such that the object keeps the same world space position, rotation and scale as before.  
  
### Description

Set the parent of the transform.

This method is the same as the [parent](Transform-parent.html) property except
that it also lets the [Transform](Transform.html) keep its local orientation
rather than its global orientation. This means for example, if the GameObject
was previously next to its parent, setting `worldPositionStays` to false will
move the GameObject to be positioned next to its new parent in the same way.  
  
The default value of `worldPositionStays` argument is true.  
  
The image below shows a child GameObject in its original position:  
  
![](../StaticFiles/ScriptRefImages/TransformSetParentOriginal.png)  
  
Here’s how it looks after calling `SetParent` with `worldPositionStays` set to
true:  
  
![](../StaticFiles/ScriptRefImages/TransformSetParentWorldTrue.png)  
  
Here’s how it looks after calling `SetParent` with `worldPositionStays` set to
false:  
  
![](../StaticFiles/ScriptRefImages/TransformSetParentWorldFalse.png)  
  
Notice how the Child Sphere is in the same position but now relative to the
New Parent Cube.

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) child;  
      
        public [Transform](Transform.html) parent;  
      
        //Invoked when a button is clicked.
        public void Example([Transform](Transform.html) newParent)
        {
            // Sets "newParent" as the new parent of the child [GameObject](GameObject.html).
            child.transform.SetParent(newParent);  
      
            // Same as above, except worldPositionStays set to false
            // makes the child keep its local orientation rather than
            // its global orientation.
            child.transform.SetParent(newParent, false);  
      
            // Setting the parent to ‘null’ unparents the [GameObject](GameObject.html)
            // and turns child into a top-level object in the hierarchy
            child.transform.SetParent(null);
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

