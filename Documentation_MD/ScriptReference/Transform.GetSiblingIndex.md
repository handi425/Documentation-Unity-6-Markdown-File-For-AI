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

#  [Transform](Transform.html).GetSiblingIndex

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

public int GetSiblingIndex();

### Description

Gets the sibling index.

Use this to return the sibling index of the GameObject. If a GameObject shares
a parent with other GameObjects and are on the same level (i.e. they share the
same direct parent), these GameObjects are known as siblings. The sibling
index shows where each GameObject sits in this sibling hierarchy.  
  
Use GetSiblingIndex to find out the GameObject’s place in this hierarchy. When
the sibling index of a GameObject is changed, its order in the Hierarchy
window will also change. This is useful if you are intentionally ordering the
children of a GameObject such as when using Layout Group components.  
  
Layout Groups will also visually reorder the group by their index. To read
more about Layout Groups see [AutoLayout](../Manual/comp-UIAutoLayout.html).
To set the sibling index of a GameObject, see
[Transform.SetSiblingIndex](Transform.SetSiblingIndex.html).

    
    
    //This script demonstrates how to return (GetSiblingIndex) and change (SetSiblingIndex) the sibling index of a [GameObject](GameObject.html).
    //Attach this script to the [GameObject](GameObject.html) you would like to change the sibling index of.
    //To see this in action, make this [GameObject](GameObject.html) the child of another [GameObject](GameObject.html), and create siblings for it.  
      
    
    using UnityEngine;  
      
    public class TransformGetSiblingIndex : [MonoBehaviour](MonoBehaviour.html)
    {
        //Use this to change the hierarchy of the [GameObject](GameObject.html) siblings
        int m_IndexNumber;  
      
        void Start()
        {
            //Initialise the Sibling Index to 0
            m_IndexNumber = 0;
            //Set the Sibling Index
            transform.SetSiblingIndex(m_IndexNumber);
            //Output the Sibling Index to the console
            [Debug.Log](Debug.Log.html)("Sibling Index : " + transform.GetSiblingIndex());
        }  
      
        void OnGUI()
        {
            //Press this [Button](UIElements.Button.html) to increase the sibling index number of the [GameObject](GameObject.html)
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, 0, 200, 40), "Add Index Number"))
            {
                //Make sure the index number doesn't exceed the Sibling Index by more than 1
                if (m_IndexNumber <= transform.GetSiblingIndex())
                {
                    //Increase the Index Number
                    m_IndexNumber++;
                }
            }  
      
            //Press this [Button](UIElements.Button.html) to decrease the sibling index number of the [GameObject](GameObject.html)
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, 40, 200, 40), "Minus Index Number"))
            {
                //Make sure the index number doesn't go below 0
                if (m_IndexNumber >= 1)
                {
                    //Decrease the index number
                    m_IndexNumber--;
                }
            }
            //Detect if any of the Buttons are being pressed
            if ([GUI.changed](GUI-changed.html))
            {
                //[Update](PlayerLoop.Update.html) the Sibling Index of the [GameObject](GameObject.html)
                transform.SetSiblingIndex(m_IndexNumber);
                [Debug.Log](Debug.Log.html)("Sibling Index : " + transform.GetSiblingIndex());
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

