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

**Experimental** : this API is experimental and might be changed or removed in
the future.

#
[GraphicsStateCollection](Experimental.Rendering.GraphicsStateCollection.html).GetGraphicsStatesForVariant

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

public void GetGraphicsStatesForVariant([Shader](Shader.html) shader,
[Rendering.PassIdentifier](Rendering.PassIdentifier.html) passId,
LocalKeyword[] keywords, List<GraphicsState> results);

## Declaration

public void
GetGraphicsStatesForVariant([Experimental.Rendering.GraphicsStateCollection.ShaderVariant](Experimental.Rendering.GraphicsStateCollection.ShaderVariant.html)
variant, List<GraphicsState> results);

### Parameters

shader | Shader used in the variant.  
---|---  
passId | PassIdentifier used in the variant.  
keywords | Array of keywords used in the variant.  
results | List of graphics states to populate.  
variant | The input variant.  
  
### Description

Populate given list with graphics states associated with input shader variant.

    
    
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.Experimental.Rendering;  
      
    public class GetGraphicsStatesExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GraphicsStateCollection](Experimental.Rendering.GraphicsStateCollection.html) graphicsStateCollection;  
      
        void Start()
        {
            List<GraphicsStateCollection.ShaderVariant> variants = new List<GraphicsStateCollection.ShaderVariant>();
            graphicsStateCollection.GetVariants(variants);
            foreach (var variant in variants)
            {
                List<GraphicsStateCollection.GraphicsState> states = new List<GraphicsStateCollection.GraphicsState>();
                graphicsStateCollection.GetGraphicsStatesForVariant(variant, states);
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

