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

#  [EditorGUI](EditorGUI.html).ObjectField

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

**Obsolete** Check the docs for the usage of the new parameter
'allowSceneObjects'.

## Declaration

public static Object ObjectField([Rect](Rect.html) position,
[Object](Object.html) obj, Type objType);

**Obsolete** Check the docs for the usage of the new parameter
'allowSceneObjects'.

## Declaration

public static Object ObjectField([Rect](Rect.html) position, string label,
[Object](Object.html) obj, Type objType);

**Obsolete** Check the docs for the usage of the new parameter
'allowSceneObjects'.

## Declaration

public static Object ObjectField([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, [Object](Object.html) obj, Type objType);

## Declaration

public static Object ObjectField([Rect](Rect.html) position,
[Object](Object.html) obj, Type objType, bool allowSceneObjects);

## Declaration

public static Object ObjectField([Rect](Rect.html) position, string label,
[Object](Object.html) obj, Type objType, bool allowSceneObjects);

## Declaration

public static Object ObjectField([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, [Object](Object.html) obj, Type objType,
bool allowSceneObjects);

### Parameters

position | Rectangle on the screen to use for the field.  
---|---  
label | Optional label in front of the field.  
obj | The object the field shows.  
objType | The type of the objects that can be assigned.  
allowSceneObjects | Allow assigning Scene objects. See Description for more info.  
  
### Returns

**Object** The object that has been set by the user.

### Description

Makes an object field. You can assign objects either by drag and drop objects
or by selecting an object using the Object Picker.

Ensure that the **allowSceneObjects** parameter is false if the object
reference is stored as part of an asset, since assets can't store references
to objects in a Scene.  
If the ObjectField is part of a custom Editor for a script component, use
EditorUtility.IsPersistent() to check if the component is on an asset or a
Scene object.  
See example in [Editor](Editor.html) class.  
  
![](../StaticFiles/ScriptRefImages/EditorGUIObjectField.png)  
_Object field in an Editor Window._

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections;  
      
    //Select the dependencies of the found [GameObject](GameObject.html)
    public class EditorGUIObjectField : [EditorWindow](EditorWindow.html)
    {
        public [GameObject](GameObject.html) obj = null;
        [[MenuItem](MenuItem.html)("Examples/Select [Dependencies](Unity.Android.Gradle.Dependencies.html)")]
        static void Init()
        {
            UnityEditor.EditorWindow window = GetWindow(typeof(EditorGUIObjectField));
            window.position = new [Rect](Rect.html)(0, 0, 250, 80);
            window.Show();
        }  
      
        void OnInspectorUpdate()
        {
            Repaint();
        }  
      
        void OnGUI()
        {
            obj = ([GameObject](GameObject.html))[EditorGUI.ObjectField](EditorGUI.ObjectField.html)(new [Rect](Rect.html)(3, 3, position.width - 6, 20), "Find Dependency", obj, typeof([GameObject](GameObject.html)));
            if (obj) {
                if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(3, 25, position.width - 6, 20), "Check [Dependencies](Unity.Android.Gradle.Dependencies.html)")) {
                    [Selection.objects](Selection-objects.html) = [EditorUtility.CollectDependencies](EditorUtility.CollectDependencies.html)(new [GameObject](GameObject.html)[] {obj});
                }  
      
                else {
                    [EditorGUI.LabelField](EditorGUI.LabelField.html)(new [Rect](Rect.html)(3, 25, position.width - 6, 20), "Missing:", "Select an object first");
                }
            }
        }
    }
    

* * *

## Declaration

public static void ObjectField([Rect](Rect.html) position,
[SerializedProperty](SerializedProperty.html) property);

## Declaration

public static void ObjectField([Rect](Rect.html) position,
[SerializedProperty](SerializedProperty.html) property,
[GUIContent](GUIContent.html) label);

## Declaration

public static void ObjectField([Rect](Rect.html) position,
[SerializedProperty](SerializedProperty.html) property, Type objType);

## Declaration

public static void ObjectField([Rect](Rect.html) position,
[SerializedProperty](SerializedProperty.html) property, Type objType,
[GUIContent](GUIContent.html) label);

### Parameters

position | Rectangle on the screen to use for the field.  
---|---  
property | The object reference property the field shows.  
objType | The type of the objects that can be assigned.  
label | Optional label to display in front of the field. Pass [GUIContent.none](GUIContent-none.html) to hide the label.  
  
### Description

Makes an object field. You can assign objects either by drag and drop objects
or by selecting an object using the Object Picker.

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

