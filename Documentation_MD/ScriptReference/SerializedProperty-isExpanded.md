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

#  [SerializedProperty](SerializedProperty.html).isExpanded

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

public bool isExpanded;

### Description

Is this property expanded in the inspector?

Serialized properties with child properties (e.g., arrays, custom serializable
structs, or custom serializable classes) may be either expanded or folded up
in the inspector to reveal or hide their children. The following example
displays a note in the inspector when users expand a
[Quaternion](Quaternion.html) property.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    [[CustomPropertyDrawer](CustomPropertyDrawer.html)(typeof([Quaternion](Quaternion.html)))]
    public class QuaternionDrawer : [PropertyDrawer](PropertyDrawer.html)
    {
        public override float GetPropertyHeight([SerializedProperty](SerializedProperty.html) property, [GUIContent](GUIContent.html) label)
        {
            // use the default property height, which takes into account the expanded state
            return [EditorGUI.GetPropertyHeight](EditorGUI.GetPropertyHeight.html)(property);
        }  
      
        public override void OnGUI([Rect](Rect.html) position, [SerializedProperty](SerializedProperty.html) property, [GUIContent](GUIContent.html) label)
        {
            // draw the default property editor
            [EditorGUI.PropertyField](EditorGUI.PropertyField.html)(position, property, label, true);  
      
            // display a warning to discourage users from manually editing child properties on a quaternion
            if (property.isExpanded)
            {
                position.height = [EditorGUIUtility.singleLineHeight](EditorGUIUtility-singleLineHeight.html);
                position.xMin += [EditorGUIUtility.labelWidth](EditorGUIUtility-labelWidth.html);
                [EditorGUI.HelpBox](EditorGUI.HelpBox.html)(position, "Editing quaternions manually is inadvisable.", [MessageType.Warning](MessageType.Warning.html));
            }
        }
    }
    

![](../StaticFiles/ScriptRefImages/SerializedPropertyIsExpanded.png)  
_Displaying a message when a Quaternion property is expanded._  
  
Note that the value of this flag is shared across all instances of the
serialized property in question that have the same property path and target
type. For example, folding up a particular property in the inspector for a
component will make the same property folded up in the inspector for all other
instances of the same component type.

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

