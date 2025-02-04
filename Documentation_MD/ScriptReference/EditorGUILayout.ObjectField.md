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

#  [EditorGUILayout](EditorGUILayout.html).ObjectField

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

public static Object ObjectField([Object](Object.html) obj, Type objType, bool
allowSceneObjects, params GUILayoutOption[] options);

## Declaration

public static Object ObjectField(string label, [Object](Object.html) obj, Type
objType, bool allowSceneObjects, params GUILayoutOption[] options);

## Declaration

public static Object ObjectField([GUIContent](GUIContent.html) label,
[Object](Object.html) obj, Type objType, bool allowSceneObjects, params
GUILayoutOption[] options);

### Parameters

label | Optional label in front of the field.  
---|---  
obj | The object the field shows.  
objType | The type of the objects that can be assigned.  
allowSceneObjects | Allow assigning Scene objects. See Description for more info.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`. Additional resources: [GUILayout.Width](GUILayout.Width.html), [GUILayout.Height](GUILayout.Height.html), [GUILayout.MinWidth](GUILayout.MinWidth.html), [GUILayout.MaxWidth](GUILayout.MaxWidth.html), [GUILayout.MinHeight](GUILayout.MinHeight.html), [GUILayout.MaxHeight](GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](GUILayout.ExpandHeight.html).  
  
### Returns

**Object** The object that has been set by the user.

### Description

Make a field to receive any object type.

You can assign objects either by drag and drop or by selecting an object using
the Object Picker.  
  
Ensure that the **allowSceneObjects** parameter is false if the object
reference is stored as part of an asset, since assets can't store references
to objects in a Scene.  
  
If the ObjectField is part of a custom Editor for a script component, use
EditorUtility.IsPersistent() to check if the component is on an asset or a
Scene object.  
  
See the example in the [Editor](Editor.html) class for further information.  
  
![](../StaticFiles/ScriptRefImages/QuickHelperObjectField.png)  
_Search for a help page by selecting the GameObject in the Object Field._

    
    
    // EditorScript that quickly searches for a help page
    // about the selected Object.
    //
    // If no such page is found in the Manual it opens the Unity forum.  
      
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [EditorWindow](EditorWindow.html)
    {
        public Object source;  
      
        [[MenuItem](MenuItem.html)("Example/[ObjectField](Search.ObjectField.html) Example _h")]
        static void Init()
        {
            var window = GetWindowWithRect<ExampleClass>(new [Rect](Rect.html)(0, 0, 165, 100));
            window.Show();
        }  
      
        void OnGUI()
        {
            [EditorGUILayout.BeginHorizontal](EditorGUILayout.BeginHorizontal.html)();
            source = [EditorGUILayout.ObjectField](EditorGUILayout.ObjectField.html)(source, typeof(Object), true);
            [EditorGUILayout.EndHorizontal](EditorGUILayout.EndHorizontal.html)();  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Search!"))
            {
                if (source == null)
                    ShowNotification(new [GUIContent](GUIContent.html)("No object selected for searching"));
                else if ([Help.HasHelpForObject](Help.HasHelpForObject.html)(source))
                    [Help.ShowHelpForObject](Help.ShowHelpForObject.html)(source);
                else
                    [Help.BrowseURL](Help.BrowseURL.html)("https://forum.unity3d.com/search.php");
            }
        }
    }
    

  
  
You can also use the **options** parameter to change the look of the control.
The following example changes the look of a Sprite ObjectField that is
displayed with a large field format.  
  
![](../StaticFiles/ScriptRefImages/SpriteObjectField.png)  
_Two different layout options for a sprite field._

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class SpriteExample : [EditorWindow](EditorWindow.html)
    {
        public [Sprite](Sprite.html) sprite;  
      
        [[MenuItem](MenuItem.html)("Example/[ObjectField](Search.ObjectField.html) [Sprite](Sprite.html) Example")]
        static void Init()
        {
            var window = GetWindowWithRect<SpriteExample>(new [Rect](Rect.html)(0, 0, 165, 100));
            window.Show();
        }  
      
        void OnGUI()
        {
            sprite = [EditorGUILayout.ObjectField](EditorGUILayout.ObjectField.html)(sprite, typeof([Sprite](Sprite.html)), false, [GUILayout.Height](GUILayout.Height.html)([EditorGUIUtility.singleLineHeight](EditorGUIUtility-singleLineHeight.html))) as [Sprite](Sprite.html);
        }
    }
    

* * *

## Declaration

public static void ObjectField([SerializedProperty](SerializedProperty.html)
property, params GUILayoutOption[] options);

## Declaration

public static void ObjectField([SerializedProperty](SerializedProperty.html)
property, [GUIContent](GUIContent.html) label, params GUILayoutOption[]
options);

## Declaration

public static void ObjectField([SerializedProperty](SerializedProperty.html)
property, Type objType, params GUILayoutOption[] options);

## Declaration

public static void ObjectField([SerializedProperty](SerializedProperty.html)
property, Type objType, [GUIContent](GUIContent.html) label, params
GUILayoutOption[] options);

### Parameters

property | The object reference property the field shows.  
---|---  
objType | The type of the objects that can be assigned.  
label | Optional label in front of the field. Pass [GUIContent.none](GUIContent-none.html) to hide the label.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](GUILayout.Width.html),
[GUILayout.Height](GUILayout.Height.html),
[GUILayout.MinWidth](GUILayout.MinWidth.html),
[GUILayout.MaxWidth](GUILayout.MaxWidth.html),
[GUILayout.MinHeight](GUILayout.MinHeight.html),
[GUILayout.MaxHeight](GUILayout.MaxHeight.html),
[GUILayout.ExpandWidth](GUILayout.ExpandWidth.html),
[GUILayout.ExpandHeight](GUILayout.ExpandHeight.html).  
  
### Description

Make a field to receive any object type.

Obsoleted. Use the overloads at the top of the page, with the
**allowSceneObjects** parameter.

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

