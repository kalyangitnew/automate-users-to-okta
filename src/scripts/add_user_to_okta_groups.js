const axios = require('axios');
const oktaConfig = require('../../okta_config/okta_config.json');

async function addUsertoOktaGroups(userId, groupId) {
  try {
    const tokenResponse = await axios.post(oktaConfig.tokenUrl, {
      grant_type: 'client_credentials',
      client_id: oktaConfig.clientId,
      client_secret: oktaConfig.clientSecret,
      scope: 'okta.groups.manage',
    });

    const accessToken = tokenResponse.data.access_token;

    await axios.post(
      '${oktaConfig.apiUrl}/groups/${groupId}/users/${userId}',
      {},
      {
        headers: {
          Authorization: 'Bearer ${accessToken}',
        },
      }
    );

    console.log('User added to Okta group successfully');
  } catch (error) {
    console.error('Error adding user to Okta group:', error.message);
  }
}

// Example usage
const userId = 'user_id_to_add'; // Replace with your user ID
const groupId = 'okta_group_id'; // Replace with your Okta group ID
addUsertoOktaGroups(userId, groupId);
