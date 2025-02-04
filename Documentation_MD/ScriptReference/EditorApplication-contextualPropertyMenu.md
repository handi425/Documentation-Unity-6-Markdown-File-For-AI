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

#  [EditorApplication](EditorApplication.html).contextualPropertyMenu

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

public static
[EditorApplication.SerializedPropertyCallbackFunction](EditorApplication.SerializedPropertyCallbackFunction.html)
contextualPropertyMenu;

### Description

Callback raised whenever the user context-clicks on a property in an
Inspector.

This callback is useful to add custom contextual menu items which can perform
operations on a particular property.

    
    
    //This script creates a new menu item named "Example" in the **Window** dropdown menu. Press this to create the Example window.  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using System.Collections;  
      
    public class Example : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Window/Example")]  
      
        public static void  ShowWindow()
        {
            [EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(Example));
        }  
      
        void OnEnable()
        {
            [EditorApplication.contextualPropertyMenu](EditorApplication-contextualPropertyMenu.html) += OnPropertyContextMenu;
        }  
      
        void OnDestroy()
        {
            [EditorApplication.contextualPropertyMenu](EditorApplication-contextualPropertyMenu.html) -= OnPropertyContextMenu;
        }  
      
        void OnPropertyContextMenu([GenericMenu](GenericMenu.html) menu, [SerializedProperty](SerializedProperty.html) property)
        {
            // show a custom menu item only for [Vector3](Vector3.html) properties
            if (property.propertyType != [SerializedPropertyType.Vector3](SerializedPropertyType.Vector3.html))
                return;  
      
            // and only when called on a [Transform](Transform.html) component
            if (property.serializedObject.targetObject.GetType() != typeof([Transform](Transform.html)))
                return;  
      
            var propertyCopy = property.Copy();
            menu.AddItem(new [GUIContent](GUIContent.html)("Randomize Vector"), false, () =>
            {
                propertyCopy.vector3Value = [Random.insideUnitSphere](Random-insideUnitSphere.html) * 5;
                propertyCopy.serializedObject.ApplyModifiedProperties();
            });
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

