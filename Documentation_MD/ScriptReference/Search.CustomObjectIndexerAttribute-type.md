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

#
[CustomObjectIndexerAttribute](Search.CustomObjectIndexerAttribute.html).type

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

public Type type;

### Description

Each time an object of a specific type is indexed, the registered function is
called.

    
    
    [CustomObjectIndexer(typeof([Shader](Shader.html)), version = 2)]
    internal static void ShaderIndexing([CustomObjectIndexerTarget](Search.CustomObjectIndexerTarget.html) context, [ObjectIndexer](Search.ObjectIndexer.html) indexer)
    {
        if (!(context.target is [Shader](Shader.html) shader) || !indexer.settings.options.properties)
            return;
    
        var ownerPropertyType = typeof([Shader](Shader.html));
        for (int i = 0, end = shader.GetPropertyCount(); i != end; ++i)
        {
            var label = shader.GetPropertyName(i);
    
            // Keep some property name patterns
            if (s_IgnorePropertyNameRx.IsMatch(label))
                continue;
    
            var name = label.ToLowerInvariant();
            if (name.Length > 0 && name[0] == '_')
                name = name.Substring(1);
            switch (shader.GetPropertyType(i))
            {
                case [ShaderPropertyType.Color](Rendering.ShaderPropertyType.Color.html):
                    var v = shader.GetPropertyDefaultVectorValue(i);
                    IndexColor(name, new [Color](Color.html)(v.x, v.y, v.z, v.w), indexer, context.documentIndex, label, ownerPropertyType);
                    break;
                case [ShaderPropertyType.Vector](Rendering.ShaderPropertyType.Vector.html):
                    v = shader.GetPropertyDefaultVectorValue(i);
                    IndexVector(name, v, indexer, context.documentIndex, label, ownerPropertyType);
                    break;
                case [ShaderPropertyType.Float](Rendering.ShaderPropertyType.Float.html):
                    indexer.IndexNumber(context.documentIndex, name, shader.GetPropertyDefaultFloatValue(i));
                    break;
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

