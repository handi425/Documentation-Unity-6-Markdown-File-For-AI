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
[AndroidApplication](Android.AndroidApplication.html).onConfigurationChanged

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

A callback to detect the device configuration changes when the application is
running.

Unity invokes this callback for the configuration changes related to the
following aspects.

  * Orientation
  * Keyboard visibility
  * Dark theme
  * Screen layout
  * Screen size

For more information on the configuration changes, refer to the [Android
developer
documentation](https://developer.android.com/guide/topics/resources/runtime-
changes).

    
    
    using UnityEngine;
    using UnityEngine.Android;  
      
    public class MyApplication : [MonoBehaviour](MonoBehaviour.html)
    {
        [AndroidConfiguration](Android.AndroidConfiguration.html) m_PrevConfig;  
      
        public void Start()
        {
            m_PrevConfig = new [AndroidConfiguration](Android.AndroidConfiguration.html)([AndroidApplication.currentConfiguration](Android.AndroidApplication-currentConfiguration.html));
            [AndroidApplication.onConfigurationChanged](Android.AndroidApplication-onConfigurationChanged.html) += OnConfigurationChanged;
        }  
      
        public void OnDisable()
        {
            [AndroidApplication.onConfigurationChanged](Android.AndroidApplication-onConfigurationChanged.html) -= OnConfigurationChanged;
        }  
      
        private void OnConfigurationChanged([AndroidConfiguration](Android.AndroidConfiguration.html) newConfig)
        {
            if (m_PrevConfig.orientation != newConfig.orientation ||
                m_PrevConfig.screenLayoutSize != newConfig.screenLayoutSize)
            {
                ApplyUIChanges(newConfig.orientation, newConfig.screenLayoutSize);
            }  
      
            if (m_PrevConfig.uiModeNight != newConfig.uiModeNight)
            {
                ApplyUINightMode(newConfig.uiModeNight);
            }  
      
            if (m_PrevConfig.screenHeightDp != newConfig.screenHeightDp ||
                m_PrevConfig.screenWidthDp != newConfig.screenWidthDp)
            {
                ApplyScreenSizeChanges();
            }  
      
            m_PrevConfig.CopyFrom(newConfig);
        }  
      
        private void ApplyUIChanges([AndroidOrientation](Android.AndroidOrientation.html) orientation, [AndroidScreenLayoutSize](Android.AndroidScreenLayoutSize.html) layoutSize)
        {  
      
        }  
      
        private void ApplyUINightMode([AndroidUIModeNight](Android.AndroidUIModeNight.html) nightMode)
        {  
      
        }  
      
        private void ApplyScreenSizeChanges()
        {  
      
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

