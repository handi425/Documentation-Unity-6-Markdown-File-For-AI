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

#  [MaterialEditor](MaterialEditor.html).RangeProperty

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

public float RangeProperty([MaterialProperty](MaterialProperty.html) prop,
string label);

## Declaration

public float RangeProperty([Rect](Rect.html) position,
[MaterialProperty](MaterialProperty.html) prop, string label);

### Parameters

label | Label for the property.  
---|---  
prop | The property to edit.  
position | Position and size of the range slider control.  
  
### Description

Draw a range slider for a range shader property.

To create a custom material editor, first you need to create the custom editor
class and save it in the Assets/Editor folder, then reference the class name
in your shader. For example:

    
    
     [CustomEditor](CustomEditor.html) "MaterialRangePropertyExample"
    

Here is an example showing a Range slider, affecting the shader's Glossiness
property:

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class MaterialRangePropertyExample : [MaterialEditor](MaterialEditor.html)
    {
        public override void OnInspectorGUI( )
        {
            serializedObject.Update( );
            [SerializedProperty](SerializedProperty.html) matShader = serializedObject.FindProperty( "m_Shader" );  
      
            if( !isVisible )
                return;  
      
            [Material](Material.html) mat = target as [Material](Material.html);
            [MaterialProperty](MaterialProperty.html) Glossiness = GetMaterialProperty( new Object[] { mat }, "_Glossiness" );  
      
            if( Glossiness == null )
                return;  
      
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)( );  
      
            RangeProperty( Glossiness, "Glossiness" );  
      
            if( [EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)( ) )
                PropertiesChanged( );
        }
    }

Here is a similar example, using the Rect parameter to position and size the
slider control within the custom material editor pane:

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class MaterialRangePropertyWithRectExample : [MaterialEditor](MaterialEditor.html)
    {
        public override void OnInspectorGUI( )
        {
            serializedObject.Update( );
            [SerializedProperty](SerializedProperty.html) matShader = serializedObject.FindProperty( "m_Shader" );  
      
            if( !isVisible )
                return;  
      
            [Material](Material.html) mat = target as [Material](Material.html);
            [MaterialProperty](MaterialProperty.html) Glossiness = GetMaterialProperty( new Object[] { mat }, "_Glossiness" );  
      
            if( Glossiness == null )
                return;  
      
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)( );  
      
            RangeProperty( new [Rect](Rect.html)( 20, 60, 300, 20 ), Glossiness, "Glossiness" );  
      
            if( [EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)( ) )
                PropertiesChanged( );
        }
    }

This is what the example editor pane looks like:  
  
![](../StaticFiles/ScriptRefImages/MaterialEditorRangeProperty.png)  
_Example material editor in Inspector._

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

