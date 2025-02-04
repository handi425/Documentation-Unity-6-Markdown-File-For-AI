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

#  [EditorGUILayout](EditorGUILayout.html).BeginFadeGroup

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

public static bool BeginFadeGroup(float value);

### Parameters

value | A value between 0 and 1, 0 being hidden, and 1 being fully visible.  
---|---  
  
### Returns

**bool** If the group is visible or not.

### Description

Begins a group that can be be hidden/shown and the transition will be
animated.

  
  
![](../StaticFiles/ScriptRefImages/EditorGUILayoutBeginFadeGroup.gif)  
_Fade Group_

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.AnimatedValues;  
      
    public class MyWindow : [EditorWindow](EditorWindow.html)
    {
        [AnimBool](AnimatedValues.AnimBool.html) m_ShowExtraFields;
        string m_String;
        [Color](Color.html) m_Color = [Color.white](Color-white.html);
        int m_Number = 0;  
      
        [[MenuItem](MenuItem.html)("Window/My Window")]
        static void Init()
        {
            MyWindow window = (MyWindow)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(MyWindow));
        }  
      
        void OnEnable()
        {
            m_ShowExtraFields = new [AnimBool](AnimatedValues.AnimBool.html)(true);
            m_ShowExtraFields.valueChanged.AddListener(Repaint);
        }  
      
        void OnGUI()
        {
            m_ShowExtraFields.target = [EditorGUILayout.ToggleLeft](EditorGUILayout.ToggleLeft.html)("Show extra fields", m_ShowExtraFields.target);  
      
            //Extra block that can be toggled on and off.
            if ([EditorGUILayout.BeginFadeGroup](EditorGUILayout.BeginFadeGroup.html)(m_ShowExtraFields.faded))
            {
                [EditorGUI.indentLevel](EditorGUI-indentLevel.html)++;
                [EditorGUILayout.PrefixLabel](EditorGUILayout.PrefixLabel.html)("[Color](Color.html)");
                m_Color = [EditorGUILayout.ColorField](EditorGUILayout.ColorField.html)(m_Color);
                [EditorGUILayout.PrefixLabel](EditorGUILayout.PrefixLabel.html)("Text");
                m_String = [EditorGUILayout.TextField](EditorGUILayout.TextField.html)(m_String);
                [EditorGUILayout.PrefixLabel](EditorGUILayout.PrefixLabel.html)("Number");
                m_Number = [EditorGUILayout.IntSlider](EditorGUILayout.IntSlider.html)(m_Number, 0, 10);
                [EditorGUI.indentLevel](EditorGUI-indentLevel.html)--;
            }  
      
            [EditorGUILayout.EndFadeGroup](EditorGUILayout.EndFadeGroup.html)();
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

