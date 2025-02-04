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

#  [GameObject](GameObject.html).Find

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

[Switch to Manual](../Manual/class-GameObject.html "Go to GameObject Component
in the Manual")

## Declaration

public static [GameObject](GameObject.html) Find(string name);

### Parameters

name | The name of the GameObject to find.  
---|---  
  
### Description

Finds and returns a GameObject with the specified name.

Only returns active GameObjects. Returns `null` if no GameObject with `name`
exists. If `name` contains a `/` character, it traverses the hierarchy like a
path name.  
  
For performance reasons, it is recommended to not use this function every
frame. Instead, cache the result in a member variable at startup, or use
[GameObject.FindWithTag](GameObject.FindWithTag.html).  
  
If the game is running with multiple scenes then `Find` will search in all of
them.  
  
To find a child GameObject, it is often easier to use
[Transform.Find](Transform.Find.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    // This returns the [GameObject](GameObject.html) named [Hand](XR.Hand.html) in one of the Scenes.  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) hand;  
      
        void Example()
        {
            // This returns the [GameObject](GameObject.html) named [Hand](XR.Hand.html).
            hand = [GameObject.Find](GameObject.Find.html)("[Hand](XR.Hand.html)");  
      
            // This returns the [GameObject](GameObject.html) named [Hand](XR.Hand.html).
            // [Hand](XR.Hand.html) must not have a parent in the [Hierarchy](UIElements.VisualElement.Hierarchy.html) view.
            hand = [GameObject.Find](GameObject.Find.html)("/[Hand](XR.Hand.html)");  
      
            // This returns the [GameObject](GameObject.html) named [Hand](XR.Hand.html),
            // which is a child of Arm > Monster.
            // Monster must not have a parent in the [Hierarchy](UIElements.VisualElement.Hierarchy.html) view.
            hand = [GameObject.Find](GameObject.Find.html)("/Monster/Arm/[Hand](XR.Hand.html)");  
      
            // This returns the [GameObject](GameObject.html) named [Hand](XR.Hand.html),
            // which is a child of Arm > Monster.
            hand = [GameObject.Find](GameObject.Find.html)("Monster/Arm/[Hand](XR.Hand.html)");
        }
    }
    

`GameObject.Find` is useful for automatically connecting references to other
objects at load time; for example, inside
[MonoBehaviour.Awake](MonoBehaviour.Awake.html) or
[MonoBehaviour.Start](MonoBehaviour.Start.html).  
  
A common pattern is to assign a GameObject to a variable inside
[MonoBehaviour.Start](MonoBehaviour.Start.html), and use the variable in
[MonoBehaviour.Update](MonoBehaviour.Update.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Find the [GameObject](GameObject.html) named [Hand](XR.Hand.html) and rotate it every frame  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [GameObject](GameObject.html) hand;  
      
        void Start()
        {
            hand = [GameObject.Find](GameObject.Find.html)("/Monster/Arm/[Hand](XR.Hand.html)");
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            hand.transform.Rotate(0, 100 * [Time.deltaTime](Time-deltaTime.html), 0);
        }
    }
    

Additional resources:
[GameObject.FindGameObjectsWithTag](GameObject.FindGameObjectsWithTag.html)

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

