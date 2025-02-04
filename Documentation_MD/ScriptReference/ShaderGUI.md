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

# ShaderGUI

class in UnityEditor

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

### Description

Abstract class to derive from for defining custom GUI for shader properties
and for extending the material preview.

Derive from this class for controlling how shader properties should be
presented. For a shader to use this custom GUI use the 'CustomEditor' property
in the shader. Note that CustomEditor can also be used for classes deriving
from MaterialEditor (search for: Custom Material Editors). Note: Only the
ShaderGUI approach works with Substance materials this is therefore the
recommended approach to custom gui for shaders. See
[ShaderGUI.OnGUI](ShaderGUI.OnGUI.html),
[ShaderGUI.OnMaterialPreviewGUI](ShaderGUI.OnMaterialPreviewGUI.html),
[ShaderGUI.OnMaterialPreviewSettingsGUI](ShaderGUI.OnMaterialPreviewSettingsGUI.html).  
  

    
    
    using System.Collections.Generic;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using System.Linq;  
      
    public class CustomShaderGUI : [ShaderGUI](ShaderGUI.html)
    {
        override public void OnGUI([MaterialEditor](MaterialEditor.html) materialEditor, [MaterialProperty](MaterialProperty.html)[] properties)
        {
            // render the shader properties using the default [GUI](GUI.html)
            base.OnGUI(materialEditor, properties);  
      
            // get the current keywords from the material
            [Material](Material.html) targetMat = materialEditor.target as [Material](Material.html);
            string[] keyWords = targetMat.shaderKeywords;  
      
            // see if redify is set, then show a checkbox
            bool redify = keyWords.Contains("REDIFY_ON");
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            redify = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("Redify material", redify);
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                // if the checkbox is changed, reset the shader keywords
                var keywords = new List<string> { redify ? "REDIFY_ON" : "REDIFY_OFF" };
                targetMat.shaderKeywords = keywords.ToArray();
                [EditorUtility.SetDirty](EditorUtility.SetDirty.html)(targetMat);
            }
        }
    }
    

### Public Methods

[AssignNewShaderToMaterial](ShaderGUI.AssignNewShaderToMaterial.html)| This
method is called when a new shader has been selected for a Material.  
---|---  
[OnClosed](ShaderGUI.OnClosed.html)| This method is called when the ShaderGUI
is being closed.  
[OnGUI](ShaderGUI.OnGUI.html)| To define a custom shader GUI use the methods
of materialEditor to render controls for the properties array.  
[OnMaterialPreviewGUI](ShaderGUI.OnMaterialPreviewGUI.html)| Override for
extending the rendering of the Preview area or completly replace the preview
(by not calling base.OnMaterialPreviewGUI).  
[OnMaterialPreviewSettingsGUI](ShaderGUI.OnMaterialPreviewSettingsGUI.html)|
Override for extending the functionality of the toolbar of the preview area or
completly replace the toolbar by not calling
base.OnMaterialPreviewSettingsGUI.  
[ValidateMaterial](ShaderGUI.ValidateMaterial.html)| When the user loads a
Material using this ShaderGUI into memory or changes a value in the Inspector,
the Editor calls this method.  
  
### Static Methods

[FindProperty](ShaderGUI.FindProperty.html)| Find shader properties.  
---|---  
  
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

