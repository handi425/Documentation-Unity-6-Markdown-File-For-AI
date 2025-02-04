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

#  [GameObject](GameObject.html).GetComponentCount

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

public int GetComponentCount();

### Returns

**int** The number of components on the GameObject as an Integer value.

### Description

Retrieves the total number of components currently attached to the GameObject.

You can use `GetComponentCount` to iterate through component indices, which is
especially convenient if used together with
[GameObject.GetComponentAtIndex](GameObject.GetComponentAtIndex.html). For
example, you can iterate through the indices to find the index of a particular
component you're interested in and then save the index for later use.

    
    
    using UnityEngine;  
      
    public class IterateComponents : [MonoBehaviour](MonoBehaviour.html)
    {
    int m_SavedComponentIndex = -1;  
      
        void Start()
        {
            //Iterate through components  on the [GameObject](GameObject.html)
            for (int i = 0; i < gameObject.GetComponentCount(); i++)
            {
                var currComponent = gameObject.GetComponentAtIndex(i);
                
                //Check if it is a [Rigidbody](Rigidbody.html) component
                if (currComponent.GetType() == typeof([Rigidbody](Rigidbody.html)) )
                {
                    m_SavedComponentIndex = i;
                }
            }  
      
            [Debug.Log](Debug.Log.html)(m_SavedComponentIndex != -1 ? $"Found component at index: {m_SavedComponentIndex}" : "Could not find component");
        }
    }
    

Additional resources:
[GameObject.GetComponentAtIndex](GameObject.GetComponentAtIndex.html)

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

