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

# VariantCompileInfo

struct in UnityEditor

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

Represents the results of compiling a variant using
[ShaderData.Pass.CompileVariant](ShaderData.Pass.CompileVariant.html).

### Properties

[Attributes](ShaderData.VariantCompileInfo.Attributes.html)| Vertex attributes
the compiled variant uses (Read Only).  
---|---  
[ConstantBuffers](ShaderData.VariantCompileInfo.ConstantBuffers.html)|
Constant buffers the compiled variant uses (Read Only). Some platforms don't
have constant buffers; however, Unity reports all global constants/uniforms in
a single constant buffer.  
[Messages](ShaderData.VariantCompileInfo.Messages.html)| Stores errors and
warnings produced during compilation (Read Only).  
[ShaderData](ShaderData.VariantCompileInfo.ShaderData.html)| Stores the raw
platform-specific bytecode for the compiled shader (Read Only).  
[Success](ShaderData.VariantCompileInfo.Success.html)| Indicates whether the
variant compilation succeeded (Read Only). If it did, it is true. Otherwise,
this is false and ShaderData.VariantCompileInfo.Messages contains the errors.  
[TextureBindings](ShaderData.VariantCompileInfo.TextureBindings.html)| Texture
bindings the compiled variant uses (Read Only).  
  
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

