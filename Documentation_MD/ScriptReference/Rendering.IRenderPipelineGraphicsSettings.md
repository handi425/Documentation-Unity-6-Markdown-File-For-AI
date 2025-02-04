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

# IRenderPipelineGraphicsSettings

interface in UnityEngine.Rendering

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

Classes implementing this interface are stored in
[RenderPipelineGlobalSettings](Rendering.RenderPipelineGlobalSettings.html).
Use them to store project default data.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.ComponentModel;
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    [
        Serializable,               // required
        Categorization.CategoryInfo("Dummy",1), Categorization.ElementInfo("A",10), // optional: sort out in the [Graphics](Graphics.html) tab
        SupportedOnRenderPipeline   // optional: which SRP support it
    ]
    public class DummyA : [IRenderPipelineGraphicsSettings](Rendering.IRenderPipelineGraphicsSettings.html)
    {
        enum Version
        {
            Initial,  
      
            Count,
            Last = Count - 1
        }
        [[SerializeField](SerializeField.html)] Version m_Version = Version.Last;
        int [IRenderPipelineGraphicsSettings.version](Rendering.IRenderPipelineGraphicsSettings-version.html) => (int)m_Version;
        bool [IRenderPipelineGraphicsSettings.isAvailableInPlayerBuild](Rendering.IRenderPipelineGraphicsSettings-isAvailableInPlayerBuild.html) => false;  
      
        // data project wise
        public int myInt = 33;
    }
    

### Properties

[isAvailableInPlayerBuild](Rendering.IRenderPipelineGraphicsSettings-
isAvailableInPlayerBuild.html)| If the setting is available in player build.  
---|---  
[version](Rendering.IRenderPipelineGraphicsSettings-version.html)| The current
version of this settings.  
  
### Public Methods

[Reset](Rendering.IRenderPipelineGraphicsSettings.Reset.html)| Optional method
to perform custom reset logic.  
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

