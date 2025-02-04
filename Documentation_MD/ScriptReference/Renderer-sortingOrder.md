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

#  [Renderer](Renderer.html).sortingOrder

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

public int sortingOrder;

### Description

Renderer's order within a sorting layer.

You can group GameObjects into layers in their
[SpriteRenderer](SpriteRenderer.html) component. This is called the
[SortingLayer](SortingLayer.html). The sorting order decides what priority
each GameObject has to the Renderer within each Sorting Layer. The lower the
number you give it, the further back the GameObject appears. The higher the
number, the closer the GameObject looks to the Camera. This is very effective
when creating 2D scroller games, as you may want certain GameObjects on the
same layer but certain parts to appear in front of others, for example,
layering clouds and making them appear in front of the sky.  
  
**Note** : The value must be between -32768 and 32767.

    
    
    //Attach a script like this to a [Sprite](Sprite.html) [GameObject](GameObject.html) (**Create** >**2D Object** >**Sprite**). Assign a [Sprite](Sprite.html) to it in the [Sprite](Sprite.html) field.
    //[Repeat](UIElements.Repeat.html) the first step for another two Sprites and make them overlap each other slightly. This shows how the order number changes the view of the Sprites.  
      
    using UnityEngine;
    public class MyScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public int MyOrder;
        public string MyName;
    }
    
    
    
    //Create a folder named “[Editor](Editor.html)” (Right click in your Assets folder, **Create** >**Folder**)
    //Put this script in the folder.
    //This script adds fields to the Inspector of your GameObjects with the MyScript script attached. Edit the fields to change the layer and order number each [Sprite](Sprite.html) belongs to.  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // Custom [Editor](Editor.html) using SerializedProperties.  
      
    [[CustomEditor](CustomEditor.html)(typeof(MyScript))]
    public class MeshSortingOrderExample : [Editor](Editor.html)
    {
        [SerializedProperty](SerializedProperty.html) m_Name;
        [SerializedProperty](SerializedProperty.html) m_Order;  
      
        private [SpriteRenderer](SpriteRenderer.html) rend;  
      
        void OnEnable()
        {
            // Fetch the properties from the MyScript script and set up the SerializedProperties.
            m_Name = serializedObject.FindProperty("MyName");
            m_Order = serializedObject.FindProperty("MyOrder");
        }  
      
        void CheckRenderer()
        {
            //Check that the [GameObject](GameObject.html) you select in the hierarchy has a [SpriteRenderer](SpriteRenderer.html) component
            if (Selection.activeGameObject.GetComponent<[SpriteRenderer](SpriteRenderer.html)>())
            {
                //Fetch the [SpriteRenderer](SpriteRenderer.html) from the selected [GameObject](GameObject.html)
                rend = Selection.activeGameObject.GetComponent<[SpriteRenderer](SpriteRenderer.html)>();
                //Change the sorting layer to the name you specify in the [TextField](UIElements.TextField.html)
                //Changes to Default if the name you enter doesn't exist
                rend.sortingLayerName = m_Name.stringValue;
                //Change the order (or priority) of the layer
                rend.sortingOrder = m_Order.intValue;
            }
        }  
      
        public override void OnInspectorGUI()
        {
            // [Update](PlayerLoop.Update.html) the serializedProperty - always do this in the beginning of OnInspectorGUI.
            serializedObject.Update();
            //Create fields for each [SerializedProperty](SerializedProperty.html)
            [EditorGUILayout.PropertyField](EditorGUILayout.PropertyField.html)(m_Name, new [GUIContent](GUIContent.html)("Name"));
            [EditorGUILayout.PropertyField](EditorGUILayout.PropertyField.html)(m_Order, new [GUIContent](GUIContent.html)("Order"));
            //[Update](PlayerLoop.Update.html) the name and order of the [Renderer](Renderer.html) properties
            CheckRenderer();  
      
            // Apply changes to the serializedProperty - always do this in the end of OnInspectorGUI.
            serializedObject.ApplyModifiedProperties();
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

