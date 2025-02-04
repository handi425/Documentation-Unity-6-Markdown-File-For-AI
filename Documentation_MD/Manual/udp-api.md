[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/udp-api.html)
  * [中文](/cn/current/Manual/udp-api.html)
  * [日本語](/ja/current/Manual/udp-api.html)
  * [한국어](/kr/current/Manual/udp-api.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/udp-api.html)
  * [中文](/cn/current/Manual/udp-api.html)
  * [日本語](/ja/current/Manual/udp-api.html)
  * [한국어](/kr/current/Manual/udp-api.html)

  * [Unity Services](UnityServices.html)
  * [Unity Distribution Portal](udp.html)
  * [UDP reference](udp-reference.html)
  * UDP API

[](udp-reference.html)

UDP reference

[](udp-sdk-data-collection.html)

UDP SDK data collection

# UDP API

**Important**  
---  
The Unity Distribution Portal (UDP) is shutting down on February 17th, 2025.
Access to the UDP Web console and services will be permanently deactivated on
this date. To download your keystores and instructions on how to republish
your games directly to app stores, visit the [UDP overview](https://api-
udp.unity.com/overview) page. If you have any questions about your account,
submit a ticket with [Unity Customer Support](https://support.unity.com/hc/en-
us/requests/new?ticket_form_id=360000323692).  
  
The UDP API lets you upload binary files to the UDP console. This lets you use
a CI system to build your app and push the output directly to UDP. Refer to
[Managing and publishing your game on the UDP console](udp-managing-and-
publishing.html#api-upload).

The following file types are supported:

  * APK
  * OBB
  * AAB

## API structure

The API is structured as follows:
https://distribute.dashboard.unity.com/developer/api/upload/:orgId/:clientId?token=xxxxxx[&obbType=xxxx]

The table below describes the parameters of the API.

Parameter | Description  
---|---  
`orgId` | The organization ID of the game for which you want to upload binary files.  
`clientId` | The client ID of the game for which you want to upload binary files.  
`token` | The authorization token generated in the UDP console, on the Developer API page.  
`obbType` | The OBB file type you want to upload. The following values are valid:  
\- `mainObb`  
\- `patchObb`  
You only need to specify this query parameter when you upload a OBB file.  
  
## Form keys

You can use form keys in the POST method to specify values when uploading your
build to UDP. The values correspond to the Binary section of the Game
Information tab.

The table below describes the form keys.

Form key | Description | Mandatory / Optional  
---|---|---  
`uploadFile` | Specify the path to the file to upload. | Mandatory  
`whatsNew` | Set the value of the field **What’s New** in the UDP console. | Optional  
`useGoogleService` | Set the value of the field **Does your game use Google Play Services?** in the UDP console. | Optional  
  
If you don’t specify optional keys, UDP uses the values of the latest version
of your game.

## Common error messages and error codes

### Invalid authentication token

If you provide an invalid authentication token, you will get an error message
with status code 401.

    
    
    {"errorCode":"NotAuthenticated","message":"not authenticated error","target":"","details":null}
    

### Invalid organization ID or client ID

If you provide an invalid organization ID or an invalid client ID, you will
get an error message with status code 400.

    
    
    {"errorCode":"InvalidParameter","message":"The given parameter is missing or invalid","target":"Invalid OrgId or ClientId","details":null}
    

### Invalid file type

If you provide an invalid file type, you will get an error message with status
code 400.

    
    
    {"errorCode":"InvalidParameter","message":"The given parameter is missing or invalid: please provide the right binary file(APK, AAB or OBB)","target":"file type","details":null}
    

### Invalid OBB type

If you provide an invalid OBB type, you will get an error message with status
code 400.

    
    
    {"errorCode":"InvalidParameter","message":"The given parameter is missing or invalid","target":"obbType","details":null}
    

### Invalid content type

If you provide an invalid content type, you will get an error message with
status code 400.

    
    
    {"errorCode":"InvalidParameter","message":"The given parameter is missing or invalid","target":"content type","details":null}
    

[](udp-reference.html)

UDP reference

[](udp-sdk-data-collection.html)

UDP SDK data collection

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

