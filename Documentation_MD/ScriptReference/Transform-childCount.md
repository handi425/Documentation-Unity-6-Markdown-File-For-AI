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

#  [Transform](Transform.html).childCount

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

public int childCount;

### Description

The number of children the parent Transform has.

**Note:** The parent is not included in the count.  
**Note:** Inactive GameObjects get included in the count.

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // generate a group of connected GameObjects
        void Awake()
        {
            [GameObject](GameObject.html) go = new [GameObject](GameObject.html)("top");  
      
            [Random.InitState](Random.InitState.html)(System.Environment.TickCount);  
      
            // add 3, 4 or 5 "middle" children that report to "top"
            for (int i = 0; i < [Random.Range](Random.Range.html)(3, 6); i++)
            {
                [GameObject](GameObject.html) go2 = new [GameObject](GameObject.html)("middle" + i.ToString());
                go2.transform.parent = go.transform;  
      
                // add between 1 to 8 "bottom" children that report to the above "middle"
                for (int j = 0; j < [Random.Range](Random.Range.html)(1, 8); j++)
                {
                    [GameObject](GameObject.html) go3 = new [GameObject](GameObject.html)("bottom" + j);
                    go3.transform.parent = go2.transform;
                }
            }
        }  
      
        void Start()
        {
            // how many children does top have?
            [GameObject](GameObject.html) go = [GameObject.Find](GameObject.Find.html)("top");
            [Debug.Log](Debug.Log.html)(go.name + " has " + go.transform.childCount + " children");  
      
            // pick a random middle group and pick a member of its children
            go = [GameObject.Find](GameObject.Find.html)("middle" + [Random.Range](Random.Range.html)(0, go.transform.childCount));
            [Debug.Log](Debug.Log.html)(go.name + " has " + go.transform.childCount + " children");
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

